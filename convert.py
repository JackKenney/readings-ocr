"""Converter from unsearchable PDFs to searchable PDFs."""
# Author: Jack Kenney
# Date: 2018/03/05

# This program requires the installation of 'pdfocr' by Geza Kovacs
# Which can be found at https://launchpad.net/~gezakovacs/+archive/ubuntu/pdfocr/+build/7671902
# Place files to be scanned in the 'readings' directory. They must be PDFs.
import os
from subprocess import call

# Determine which files to convert and move
names = []
for root, dirs, files in os.walk("./readings"):
    for file in files:
        if file.endswith(".pdf"):
            names.append(file)
# Make sure the OCR directory has been created.
if not os.path.isdir("searchable/pdf"):
    call(["mkdir", "-p", "searchable/pdf"])
if not os.path.isdir("searchable/txt"):
    call(["mkdir", "-p", "searchable/txt"])
if not os.path.isdir("read"):
    call(["mkdir", "-p", "read"])

# Begin
for name in names:
    name = name[0 : len(name) - 4]
    read = "./readings/" + name + ".pdf"
    out = "./searchable/pdf/" + name + "-OCR.pdf"
    # Convert the files
    call(["pdfocr", "-i", read, "-o", out])
    # Move files to read
    call(["mv", "readings/" + name + ".pdf", "read/" + name + ".pdf"])

call(["sh", "text.sh"])  # make txt files

# Sources for python scripting:
# https://docs.python.org/3/library/os.html#os.fwalk
# https://stackoverflow.com/questions/1274506/how-can-i-create-a-list-of-files-in-the-current-directory-and-its-subdirectories
# https://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
