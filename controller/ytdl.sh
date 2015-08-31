#!/bin/bash

# for use with NNDController; 

# $1 should be the fully formed url, i.e. http://www.nicovideo.jp/watch/sm26849449
# $2 should be the id only, i.e. sm26849449

youtube-dl -o $2 $1
