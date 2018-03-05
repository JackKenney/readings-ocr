#!/bin/bash
for f in ./searchable/txt/*; 
do echo $f; 
cat $f | grep -i "$1"; 
done
