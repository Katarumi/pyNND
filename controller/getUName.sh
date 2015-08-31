# Extracts username from a raw myList page.

#!/bin/bash

cat $1 | sed '/.*nickname:/!d' >> testout
cat testout | sed -n 's/nickname: \"/&\n/;s/.*\n//p' >> testout2	
cat testout2 | sed 's/\".*//' >> final

rm testout
rm testout2
