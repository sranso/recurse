# This lives in ~/Users/sranso/bin but I wanted to add a copy here

#!/bin/bash

PURPLE='\033[1;35m'

function grabAffirmation {
  local FILE=$1
  local LINES=$(wc -l < $FILE)
  local LINE=$(getRandomNumberInLines $LINES)
  echo -e "${PURPLE}***************************"
  echo -e "${PURPLE}$(head -n $LINE $FILE | tail -1)"
  echo -e "${PURPLE}***************************"
}

function getRandomNumberInLines {
  echo $[ ( $RANDOM % $1 ) + 1 ]
}

grabAffirmation /Users/sranso/bin/affirmations.txt

# First attempt:

#AFFIRMATION=''
#while IFS='' read -r line || [[ -n "$line" ]]; do
#  AFFIRMATION=$line
#done < "$1"
#echo $AFFIRMATION
