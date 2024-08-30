# /bin/bash

if [ "$#" -ne 2 ];
	then echo "illegal number of parameters: first parameter is folder name and second is file extension"
fi

find $1 -type f -name "*.$2"

