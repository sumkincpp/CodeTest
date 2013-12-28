#!/usr/bin/perl

use Mojo::UserAgent;
use Mojo::IOLoop;
my $res = [
  ['10.100.230.3'], ['10.107.230.4'], ['10.81.230.6'], ['10.97.230.231'], ['172.17.129.4'], ['172.17.130.132'],
  ['172.17.165.214'], ['172.17.172.4'], ['172.17.183.5'], ['172.17.98.9'], ['172.25.230.4'], ['172.25.230.5']
];
my $ua = Mojo::UserAgent->new;
$ua    = $ua->connect_timeout(2);
foreach my $ip (@{$res}) {
  my $host = $ip->[0];
  $ua->post("http://$host/login.cgi" => form => { user => 'user', pwd  => 'secret' }
  => sub {
    my ($ua, $tx) = @_;
    if ($tx->success) {
        $ua->get("http://$host/status/" => sub {

             my ($ua, $tx) = @_;
             print $tx->remote_address() , " uptime: ",
             $tx->res->dom->find('font')->[10]->text,

             "\n";
             });
    }
    else {
      print "$host down\n";
    }
    Mojo::IOLoop->stop;
  });
  Mojo::IOLoop->start;
}
