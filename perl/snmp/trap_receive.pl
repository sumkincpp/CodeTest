#!/usr/bin/perl

use strict;
use Sys::Hostname;
use IO::Socket;
use Convert::BER;
use Convert::BER qw(/^(\$|BER_)/);

my $FAILED    = "FAILED!";
my $opt_write = 0;
my $opt_dir   = "";

if ((my $ret = &snmptrapd($opt_write, $opt_dir)) =~ $FAILED) {
    printf "%-25s     -> SNMPTrap Server Error!\n\n", $ret;
    exit 1
}

exit;

########################################################
# SNMP Trapd #
##############
sub snmptrapd () {

    my ($wr, $dir) = @_;

    my @traptypes = qw(COLDSTART WARMSTART LINKDOWN LINKUP AUTHFAIL EGPNEIGHBORLOSS ENTERPRISESPECIFIC);
    my @trap      = qw(version community ent_OID agentaddr generic_trap specific_trap timeticks ber_varbindlist);

    my $sock = IO::Socket::INET->new(LocalPort => '162',
                                         Proto => 'udp'
                                    ) || return $FAILED . " (Cannot open port)";

    print "Starting MODE                 -> SNMPTrap Server\n";
    printf "Listening on                  -> %s:162 (udp)\n", inet_ntoa((gethostbyname(hostname))[4]);

    if ($wr) {

        my $outfile;
        if (defined($dir)) {
            $outfile = $dir . "/"
        }

        $outfile .= "snmptrapd.log";

        print "Logging to                    -> $outfile\n"
    }
    print "\n";

    my $ber = new Convert::BER;
    $ber->define(
                 [ Trap_PDU  => $SEQUENCE, BER_CONTEXT | BER_CONSTRUCTOR | 0x04 ],
                 [ Trap2_PDU => $SEQUENCE, BER_CONTEXT | BER_CONSTRUCTOR | 0x07 ],
                 [ IpAddress => $STRING,   BER_APPLICATION               | 0x00 ],
                 [ Counter   => $INTEGER,  BER_APPLICATION               | 0x01 ],
                 [ Gauge     => $INTEGER,  BER_APPLICATION               | 0x02 ],
                 [ TimeTicks => $INTEGER,  BER_APPLICATION               | 0x03 ],
                 #[ Opaque    => undef,     BER_APPLICATION               | 0x04 ]
                );

    my $buf;
    while (1) {

        $sock->recv($buf, 1500);
        my ($port, $ipaddr) = sockaddr_in($sock->peername);

        #DEBUG: print "BUF = $buf\n";

        #my $host = gethostbyaddr($ipaddr, AF_INET);
        my $host = inet_ntoa($ipaddr);

        my %trap;
        $ber->buffer($buf);

        # Can't get BER to do some smart recursion, so we need to get the top part of the 
        # packet to determine SNMP v1 or v2c and then use different BER decode routines.
        $ber->decode(
                     SEQUENCE => [
                                  INTEGER => \$trap{'version'},
                                   STRING => \$trap{'community'},
                                      ANY => \$trap{'rest_of_pdu'}
                                 ]
                    );

        #DEBUG: print "REST = $trap{'rest_of_pdu'}[0]\n";

        $ber->buffer($trap{'rest_of_pdu'}[0]);

        # SNMP version 1
        if ($trap{'version'} == 0) {

            # Instead of getting the varbindlist here and in v2c, we'll just put the rest 
            # of the packet into the $trap{'ber_varbindlist'} variable and deal with it later.
            $ber->decode(
                         Trap_PDU => [
                                      OBJECT_ID => \$trap{'ent_OID'},
                                      IpAddress => \$trap{'agentaddr'},
                                        INTEGER => \$trap{'generic_trap'},
                                        INTEGER => \$trap{'specific_trap'},
                                      TimeTicks => \$trap{'timeticks'},
                                   #SEQUENCE_OF => [
                                                    ANY => \$trap{'ber_varbindlist'}
                                   #               ]
                                     ]
                        )

        # SNMP version 2c
        } elsif ($trap{'version'} == 1) {
            $ber->decode(
                         Trap2_PDU => [
                                       INTEGER => \$trap{'request_ID'},
                                       INTEGER => \$trap{'error_status'},
                                       INTEGER => \$trap{'error_index'},
                                  #SEQUENCE_OF => [
                                                   ANY => \$trap{'ber_varbindlist'}
                                  #               ]
                                      ]
                        )

        # SNMP version IDon'tKnow
        } else {
            printf STDERR "%s\t%s\t%i\tUNRECOGNIZED PDU VERSION", yyyymmddhhmmss(), $host, $port;
            next
        }

        #DEBUG: print "VARBINDLIST = $trap{'ber_varbindlist'}[0]\n";

        my $varbind;
        my @oid;
        my @val;

        $ber->buffer($trap{'ber_varbindlist'}[0]);
        $ber->decode(
                     SEQUENCE_OF => [ \$varbind,
                                     SEQUENCE => [
                                                  OBJECT_ID => sub { $oid[$_[0]] = undef; \$oid[-1] },
                                                     CHOICE => [ undef,
                                                                   STRING => sub { $val[$_[0]] = undef; \$val[-1] },
                                                                  INTEGER => sub { $val[$_[0]] = undef; \$val[-1] },
                                                                  Counter => sub { $val[$_[0]] = undef; \$val[-1] },
                                                                    Gauge => sub { $val[$_[0]] = undef; \$val[-1] },
                                                                TimeTicks => sub { $val[$_[0]] = undef; \$val[-1] },
                                                                OBJECT_ID => sub { $val[$_[0]] = undef; \$val[-1] }
                                                               ]
                                                 ]
                                    ]
                    );

        my $p;
        if ($trap{'version'} == 0) {
            $p = sprintf "%s\t%s\t%i\t%i\t%s\t%s\t%s\t%s\t%s\t%s\t", yyyymmddhhmmss(), $host, $port, $trap{'version'} + 1, $trap{'community'}, $trap{'ent_OID'}, inet_ntoa($trap{'agentaddr'}), $traptypes[$trap{'generic_trap'}], $trap{'specific_trap'}, $trap{'timeticks'}
        } elsif ($trap{'version'} == 1) {
            $p = sprintf "%s\t%s\t%i\t%i\t%s\t%s\t%s\t%s\t", yyyymmddhhmmss(), $host, $port, $trap{'version'} + 1, $trap{'community'}, $trap{'request_ID'}, $trap{'error_status'}, $trap{'error_index'}
        } else {}

        for (0..$#oid) {
            $p .= $oid[$_] . ": " . $val[$_] . "; "
        }
        $p .= "\n";

        # Print to screen
        print $p;

        # Print to logfile        
        if ($wr) {

            my $outfile;
            if (defined($dir)) {

                # Create directory if it doesn't exist
                if (!(-e $dir)) { mkdir ($dir) }
                $outfile = $dir . "/"
            }

            $outfile .= "snmptrapd.log";

            if (open(OUT, ">>$outfile")) {
                print OUT $p;
                close(OUT)
            } else {
                print STDERR "$0: cannot open outfile - $outfile\n"
            }
        }
    }
}

########################################################
# YYYYMMDDHHMMSS Timestamp #
############################
sub yyyymmddhhmmss {

    my @time = localtime();
    return (($time[5] + 1900) . ((($time[4] + 1) < 10)?("0" . ($time[4] + 1)):($time[4] + 1)) . (($time[3] < 10)?("0" . $time[3]):$time[3]) . (($time[2] < 10)?("0" . $time[2]):$time[2]) . (($time[1] < 10)?("0" . $time[1]):$time[1]) . (($time[0] < 10)?("0" . $time[0]):$time[0]))
}
