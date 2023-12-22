#!/bin/bash
for f in ../assets/img/*.jpg;
do 
    echo "Processing $f file..."; 
    ./cwebp -q 50 $f -o $f-lg.webp
    ./cwebp -resize 480 0 -q 50 $f -o $f.webp
    ./cwebp -resize 120 0 -q 50 $f -o $f-mini.webp
done