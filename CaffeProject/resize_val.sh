FOLDER=./

for name in $FOLDER/val/*.jpg;
do
	convert -resize 256x256\! $name $name
done
