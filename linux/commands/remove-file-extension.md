#!/bin/bash

filename=this.is.not.a.file.txt 

echo $(basename $filename .txt)

echo Parameter expension is power

echo Removing last whatever extension -- txt
echo "${filename%.*}"

echo Removing all after dot
echo "${filename%.*}"

echo $filename | rev | cut -f 2- -d '.' | rev

echo $filename | sed -e 's/\.[^./]*$//'

echo dotfiles case 
echo .txt | sed -re 's/(^.*[^/])\.[^./]*$/\1/'
