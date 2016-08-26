#!/usr/bin/perl
#Retrieved from "http://wiki.crc.nd.edu/wiki/index.php/Convert_CSV_To_Wiki_Table"
open(INPUT, "< input.csv")
       or die "Couldn't open file for reading: $!\n";
open(OUTPUT, "> mediawiki.mw")
       or die "Couldn't open file for writing: $!\n";   

while (<INPUT>) {
       @fields = split(",");
       printf OUTPUT ("\|$fields[0]\n\|$fields[1]\n\|$fields[2]\n\|$fields[3]\|-\n");
}
close INPUT;
close OUTPUT;
