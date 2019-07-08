#!/usr/bin/env bash
dir_in=./data/LGAD2/100
for file in ${dir_in}/*
do
sed -i '1, 6d' $file
sed -i 's/,/  /g' $file
done


## filelist=`ls ~xiaosy/disk/scratchfs/lgad/data/LGAD2/50/`
## for file in $filelist
## do
## # #   echo 'I'
## # #   file_out=change_${file}
## # #   echo 'hello'
## sed '1, 6d' $file
## sed -i 's/,/  /g' $file
## done
