# Extracts title from a video page.

#!/bin/bash

# $1 should be the fully formed url to the page.

#curl $1 > temp.out
cat temp.out | sed '/.*og:title/!d' > testout
cat testout | sed -n 's/content=\"/&\n/;s/.*\n//p' > testout2
cat testout2 | sed 's/\".*//' > testout
cat testout | sed 's/[^.*】 ]*\(】 *\)//' > testout2
cat testout2 | sed 's/ 【.*//' > final

rm testout
rm testout2
