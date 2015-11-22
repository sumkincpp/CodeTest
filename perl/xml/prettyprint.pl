# http://stackoverflow.com/questions/8225194/html-indenting-with-perl
use HTML::HTML5::Parser qw();
use HTML::HTML5::Writer qw();
use XML::LibXML::PrettyPrint qw();

print HTML::HTML5::Writer->new(
    start_tags => 'force',
    end_tags => 'force',
)->document(
    XML::LibXML::PrettyPrint->new_for_html(
        indent_string => "\t"
    )->pretty_print(
        HTML::HTML5::Parser->new->parse_string(
            '<!DOCTYPE html><html><head><title>test</title></head>   <body>  <h1>hello!</h1><p>It works!</p></body></html>'
        )
    )
);
