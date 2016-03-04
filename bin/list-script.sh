#!/bin/sh
for i in `cat line-list.txt | awk '{ print $1 }'`
do
  ls ${i}/a*.txt | sed 's/^.*a_//; s/.txt.*$//' > ${i}/list.txt
done

