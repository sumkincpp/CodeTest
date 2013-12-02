#!/usr/local/bin/perl
      
use strict;
use EV;
use AnyEvent::HTTP;
use Coro;
  
$AnyEvent::HTTP::MAX_PER_HOST = 2;
  
opendir D, '.';
mkdir ('audio', 0755) unless (readdir D) =~ /audio/;
closedir D;
  
my $file = 'audio.htm';
  
open (F, $file) or die "Can't open audio.htm";
  
my $page = join ('', <F>);
  
my %mp3;
while ($page =~ m{value="(http://.*?mp3).*?return false">(.*?)</a>.*?<span class="title">(.*?)</span>}sgi){
    my $url = $1;
    my $name1 = $2;
    my $name2 = $3;
    $name1 =~ s%<.*>|[!@$#^&*();:"<>?]%%g;
    $name2 =~ s%<.*>|[!@$#^&*();:"<>?]|\s$%%g;
    $mp3 {$url} = $name1.($name2 ? ' - '.$name2 : '').'.mp3';
}
delete $mp3 {''};
  
close (F);
  
foreach my $url (keys %mp3){
    my $filename = $mp3 {$url};
      
    if ($filename and (not -e "audio/$filename" or -z "audio/$filename")){
        do {
            http_get (
                $url,
                sub {
                    my ($content) = @_;
                      
                    open (MP3, ">audio/$filename");
                    binmode (MP3);
                    print MP3 $content;
                    close (MP3);
                      
                    print $filename." DOWNLOADED\n";
                }
            );
        } while (-z "audio/$filename");
    }
}
  
EV::run;
