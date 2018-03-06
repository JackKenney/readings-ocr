#!/bin/bash
# Converts PDFs to TXT files and moves them to txt folder
for f in ./searchable/pdf/*.pdf;
    do echo "$f";
    pdftotext "$f";
done
mv *.txt ../txt/