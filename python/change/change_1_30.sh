#!/usr/bin/env bash
dir_in=../../data/LGADtimeresolution/30
for file in ${dir_in}/*
do
sed -i '1, 6d' $file
# sed -i 's/,/  /g' $file
done


