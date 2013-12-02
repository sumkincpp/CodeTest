#!/usr/bin/perl
use strict;
use AnyEvent;
use AnyEvent::HTTP;
use Time::HiRes qw(time);

my $cv = AnyEvent->condvar( cb => sub {
    warn "done";
});

my $urls = ["https://www.google.com",
            "http://www.windley.com/",
            "https://www.bing.com",
            "http://www.example.com",
            "http://www.wetpaint.com",
            "http://www.uh.cu"
            ];


my $start = time;
my $result;

$cv->begin(sub { shift->send($result) });


for my $url (@$urls) {
  $cv->begin;

  my $now = time;
  my $request;  

  $request = http_request(
    GET => $url, 
    timeout => 2, # seconds
    sub {
      my ($body, $hdr) = @_;
      if ($hdr->{Status} =~ /^2/) {
        push (@$result, join("\t", ($url,
          " has length ",
          $hdr->{'content-length'}, 
          " and loaded in ",
          time - $now,
          "ms"))
        );
      } else {
        push (@$result, join("",
          "Error for ",
          $url,
          ": (", 
          $hdr->{Status}, 
          ") ", 
          $hdr->{Reason})
        );
      }
      undef $request;
      $cv->end;
    }
  );
}

$cv->end;

warn "End of loop\n";

my $foo =   $cv->recv;

print join("\n", @$foo), "\n" if defined $foo;

print "Total elapsed time: ", time-$start, "ms\n";
