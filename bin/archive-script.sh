#!/bin/bash

for i in `cat line-list.txt | awk '{ print $1 }'`
do
  grep -E "^${i} " a_*.txt | sed 's/^a_//; s/.txt.*$//' > ${i}/list.txt
done


for i in `cat line-list.txt | awk '{ print $1 }'`
do
  for j in `cat ${i}/list.txt`
  do
    echo ${i}/${j}
    mv ?_${j}.txt ${i}
  done
done

