#!/bin/bash

TRAIN_FOLDER=./train
VAL_FOLDER=./val

TRAIN=./train.txt
VAL=./val.txt

if [ ! -d "$TRAIN_FOLDER" ];
then
	echo "Please check whether your train folder or val folder exists"
	exit
fi

rm *.txt

if [[ ! -f $TRAIN ]]; then
	touch $TRAIN
fi

if [[ ! -f $VAL ]]; then
	touch $VAL
fi

for file in `ls "$TRAIN_FOLDER" | grep erosberry`
do
	echo $file" 0" >> $TRAIN
done

for file in `ls "$TRAIN_FOLDER" | grep normal`
do
	echo $file" 1" >> $TRAIN
done

for file in `ls "$VAL_FOLDER" | grep erosberry`
do
	echo $file" 0" >> $VAL
done

for file in `ls "$VAL_FOLDER" | grep normal`
do
	echo $file" 1" >> $VAL
done