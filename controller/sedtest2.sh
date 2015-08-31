#!/bin/bash


# Args:
# $1: raw Utaite mylist; 
# $2: Final output.

# Old args:
# x$2: Cut bit from $5, starting with :"sm, now cutSM 
# x$3: the first ten characters of $2, appended. now smlist
# $4: Final output.
# x$5: Copy of $1, destroyed. Now temp

a=1
sp="/-\|"
echo -n ' '

cp $1 temp

#cat temp | sed '0,/.*:\"sm/s//sm/' > cutSM
awk '/sm[0-9]/{print}' temp > cutSM 
cut -c 1-10 cutSM >> smlist
ccount=$(wc -m < cutSM) 
oldcount=0 


while [ "$ccount" -ne $oldcount ]

do
	sed -r -i 's/.{77}$//' temp 
	cat temp | sed '0,/.*video_id\":\"sm/s//sm/' > cutSM
	cut -c 1-10 cutSM >> smlist
	oldcount=$ccount
	ccount=$(wc -m < cutSM)
    	printf "\b${sp:a++%${#sp}:1}"

done

awk 'length($0)>9' smlist > awktemp 
#uniq awktemp > uniqtemp 
grep -e '^sm' awktemp > greptemp 
uniq greptemp > $2
rm awktemp
#rm uniqtemp
rm greptemp
rm temp
rm cutSM
rm smlist

./getUName.sh $1
echo -e '0r final\nw' | ed $2
rm final
