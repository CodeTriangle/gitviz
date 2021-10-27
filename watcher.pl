use strict;
use warnings;
use utf8;

sub reload {
    `git log --all --oneline --graph`;
}

%SIG{USR1} = \&reload;
