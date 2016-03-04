#!/bin/sh

awk '{ print $1 }' a*.txt | sed '/^$/d' | sort | uniq -c | sort -rn | awk '{ print $2 "\t" $1 }' > line-list.txt 

