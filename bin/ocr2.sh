#!/bin/sh
pdftk track-and-route.pdf burst

for i in `ls pg_*.pdf | sed 's/^pg_//; s/.pdf$//'`
do
    echo ${i}

    pdftoppm pg_${i}.pdf -singlefile -r 600 a_${i} -x 420 -y 750 -W 6500 -H 125
    convert a_${i}.ppm a_${i}.tif
    tesseract a_${i}.tif a_${i} -l eng -psm 6 
    rm a_${i}.ppm a_${i}.tif

    pdftoppm pg_${i}.pdf -singlefile -r 600 b_${i} -x 420 -y 1050 -W 1200 -H 3500
    convert -threshold 50% b_${i}.ppm b_${i}.tif
    tesseract b_${i}.tif b_${i} -l eng -psm 7 
    rm b_${i}.ppm b_${i}.tif

    pdftoppm pg_${i}.pdf -singlefile -r 600 c_${i} -x 420 -y 1050 -W 1650 -H 3500
    convert -threshold 50% c_${i}.ppm c_${i}.tif
    tesseract c_${i}.tif c_${i} -l eng -psm 6 
    rm c_${i}.ppm c_${i}.tif

    pdftoppm pg_${i}.pdf -singlefile -r 600 d_${i} -x 4925 -y 1050 -W 1550 -H 3500
    convert -threshold 50% d_${i}.ppm d_${i}.tif
    tesseract d_${i}.tif d_${i} -l eng -psm 6 
    rm d_${i}.ppm d_${i}.tif
done

