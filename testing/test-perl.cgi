#!/usr/bin/perl -w

my $input = <STDIN>;
open(FILE, ">", "/var/www/html/webapp/testing/output.txt") 
	or die "cannot open > output.txt: $!";
print FILE $input."\n";
close(FILE);
#Header must end with a blank line, thus two new lines
$retMsg = '<!doctype html>\n\n';
#Enclosing JSON object in array, because that's what google did
$retMsg += '[\n';
$retMsg += '{"response":"Got your message"}';
#End of message.  Need to send signal?
$retMsg += '\n';
$retMsg += '\n';

#Transmit
print $retMsg;
