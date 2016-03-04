#!/bin/sh

for i in `cat line-list.txt | awk '{ print $1 }'`
do
  echo ${i}; cd ${i}
  ../../bin/process2.py list.txt > ${i}.tsv
  cd ..
done

for i in `cat line-list.txt | awk '{ print $1 }'`
do
  #concatenate all line reports and calculate the combined distance (miles.chains)
  cat ${i}/${i}.tsv | awk 'BEGIN { FS="\t"} { print $_ "\t" $7"."$8 }' | sed 's/\.5$/5/'
done | tee output.tsv


