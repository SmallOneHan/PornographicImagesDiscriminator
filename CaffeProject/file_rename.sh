#!/bin/bash

PREFIX_NAME=$1
WORK_DIR=./$PREFIX_NAME
if [ ! -d "$WORK_DIR" ]; then
	echo "Please Check whether your input directory exist!"
fi

declare -i num=0
for file in `ls $WORK_DIR *.jpg` 
do
	SRC="$WORK_DIR/$file"
	DEST="$WORK_DIR/$PREFIX_NAME-$num.jpg"
	mv $SRC $DEST
	echo "Rename $SRC to $DEST"
	num=$((num+1))
done
