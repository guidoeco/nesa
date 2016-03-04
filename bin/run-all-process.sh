# process files in all regions and generate corresponding report in output.tsv
# run in nesa directory 
for i in `cat regions.txt`
do
  cd ${i}
  ../bin/run-process.sh
  cd ..
done
