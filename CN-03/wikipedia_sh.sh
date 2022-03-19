#!/bin/sh

if [ $# == "0" ]
then
	echo "Enter the article title: "
	read art_title
else
	art_title=$*
	
fi

echo "Title: $art_title"

article_title=${art_title// /%20}


url="https://en.wikipedia.org/w/api.php?action=query&format=json&titles=$article_title&prop=extracts"

status_code=$( curl --write-out %{http_code} --silent --output /dev/null $url )

echo "Response Status Code: $status_code"

if [ $status_code == "200" ]
then
	echo $url >> logfile_sh.txt
else
	echo "Error: Failed to fetch data"
fi
