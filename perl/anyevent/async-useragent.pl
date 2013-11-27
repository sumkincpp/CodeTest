#!/usr/bin/perl
use AnyEvent::HTTP::LWP::UserAgent;
use AnyEvent;

my $ua = AnyEvent::HTTP::LWP::UserAgent->new;
my @urls = (...);
my $cv = AE::cv;
$cv->begin;
foreach my $url (@urls) {
    $cv->begin;
    $ua->get_async($url)->cb(sub {
        my $r = shift->recv;
        print "url $url, content " . $r->content . "\n";
        $cv->end;
    });
}
$cv->end;
$cv->recv;
