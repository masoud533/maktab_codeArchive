#! /bin/bash
clear
read -p "enter download link:    " link

wget $link

touch download_dict.txt
echo download link is:  $link > download_dict.txt

clear
sleep 1
echo -n 'procesing .'
sleep 0.5
echo -n "."
sleep 0.5
echo -n "."
sleep 2
clear
echo download is  done!!!!
