#!/bin/bash
for f in ../assets/img/*.jpg;
do 
    echo "Processing $f file..."; 
    ./cwebp -q 50 $f -o $f.webp
done