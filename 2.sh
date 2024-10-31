# /bin/bash

if [ $# -ne 2 ]; then
	echo "usage: $0 <path> <text>"
	exit 1
fi

grep -rl "$2" "$1"
