#!/usr/bin/perl -w

my $input = <STDIN>;
open(FILE, ">", "output.txt") 
	or die "cannot open > output.txt: $!";
print FILE $input."\n";
close(FILE);
print '{"response":"Got your message"}';
