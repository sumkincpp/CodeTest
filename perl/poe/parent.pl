#!/usr/bin/perl
#-----------------------------------------------------------------------
# main.pl

use strict;
use warnings;

use POE qw(Wheel::Run Filter::Line);

sub _start {
    my ($kernel, $heap) = @_[KERNEL, HEAP];

    $heap->{'child'} = POE::Wheel::Run->new(
        'CloseEvent'   => 'child_close',
        'Program'      => ['perl', 'child.pl'],
        'StderrEvent'  => 'child_stderr',
        'StdoutEvent'  => 'child_stdout',
        'StdioFilter'  => POE::Filter::Line->new(),
        'StderrFilter' => POE::Filter::Line->new()
    );

    $kernel->sig_child($heap->{'child'}->PID, 'sig_chld');
    $heap->{'child'}->put("user\npw\n");
}

sub child_close {
    my ($kernel, $heap) = @_[KERNEL, HEAP];

    delete($heap->{'child'});
}

sub child_stderr {
    my $stderr = $_[ARG0];

    print("$stderr\n");
}

sub child_stdout {
    my $stdout = $_[ARG0];

    print("$stdout\n");
}

sub sig_chld {
}

POE::Session->create(
    inline_states => {
        '_start'       => \&_start,
        'child_close'  => \&child_close,
        'child_stderr' => \&child_stderr,
        'child_stdout' => \&child_stdout,
        'sig_chld'     => \&sig_chld
    }
);

POE::Kernel->run();
exit(0);
