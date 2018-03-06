#!/bin/bash
# Simply searches for first argument (given as string)
# And returns list of files containing string.
cat ./searchable/txt/* | grep -rl "$1"; 
