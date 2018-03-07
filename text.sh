#!/bin/bash
# Converts PDFs to TXT files and moves them to txt folder
for f in ./searchable/pdf/*.pdf;
    do echo "$f";
    pdftotext "$f";
done
mv searchable/pdf/*.txt searchable/txt/
# mv ./searchable/pdf/*.txt ./searchable/txt/