#!/bin/bash
# Converts PDFs to TXT files and moves them to txt folder
for f in ./searchable/pdf/*.pdf;
    do 
    echo "$f";
    pdftotext "$f";
done
for g in ./searchable/pdf/*.txt;
    do 
    echo "$g";
    tr '[:upper:]' '[:lower:]' < "$g" >> 'temp.txt';
    mv 'temp.txt' "$g";
done
mv searchable/pdf/*.txt searchable/txt/
# mv ./searchable/pdf/*.txt ./searchable/txt/