#!/bin/bash
echo "" > solutions.pdf &&
rm solutions.pdf &&
./../py2pdf.sh ./solutions/exo1.py && 
./../py2pdf.sh ./solutions/exo2.py &&
mv ./solutions/*.py.pdf . &&
pdftk *.pdf cat output solutions.pdf && 
/home/bouscadilla/scripts/Multimedia/applatir_pdf.sh solutions.pdf &&
mv solutions.pdf.pdf solutions.pdf
rm exo1.py.pdf exo2.py.pdf