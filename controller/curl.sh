#!/bin/bash
counter=0 
while IFS='' read -r line || [[ -n "$line" ]]; do
	let counter=counter+1
	curl "$line" > $counter.html
done < "$1"
