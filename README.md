This is an extract of the Network Rail (NR) NESA data downloaded as embedded tifff pdf from the Network Rail National Electronic Sectional Appendix (http://www.networkrail.co.uk/aspx/10563.aspx)
The accompanying data is some years old and is based on OCR extract of the pdf files then reviewed and converted into a tsv format, by region and line.

The regions are:
Region				URL
Anglia				http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/anglia%20sectional%20appendix.pdf
Kent, Sussex and Wessex		http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/kent%20sussex%20wessex%20sectional%20appendix.pdf
London North Eastern 		http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/london%20north%20eastern%20sectional%20appendix.pdf
London North Western (north)	http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/london%20north%20western%20north%20sectional%20appendix.pdf
London North Western (south)	http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/london%20north%20western%20south%20sectional%20appendix.pdf
Scotland     	     		http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/scotland%20sectional%20appendix.pdf
Wessex
Western				http://www.networkrail.co.uk/browse%20documents/sectional%20appendix/western%20sectional%20appendix.pdf

The logical process to create the NESA files by line then is something like the following.

Please note that this approximates and is *not* the actual command line used to generate the final files. This is due to data quality issues with the raw scans and the iterative way in which the text files were manually hacked along with changes the process2.py script

0) Add nesa/bin directory to the path variable

1) Download:
$ loop (region, url) 
$ do
$   cd $region
$   wget URL > track-and-route.pdf
$ done

2) Process track-and-route.pdf file to generate raw scanned text files
$ for region in `cat regions.txt`
$ do
$   cd $region
$   ocr2.sh
$   mkdir archive
$   mv pg_*.pdf archive
$   cd ..
$ done

3) Create line-number directories and move ocr files to archive directory
$ for region in `cat regions.txt`
$ do
$   cd $region
#   create line-list.txt file
$   line-list.sh
#   create and move ocr files to line-number directories
$   archive-script.sh
$ done

4) Create line reports and combined region report
$ for region in `cat regions.txt`
$ do
$   cd $region
$   run-process.sh
$ done
