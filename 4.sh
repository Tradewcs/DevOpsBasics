#!/bin/bash

usage() {
    echo "usage: $0 <path> <text>"
    exit 1
}

if [ $# -ne 2 ]; then
    usage
fi

directory=$1
extension=$2

if [ ! -d "$directory" ]; then
    echo "Directory $directory does not exists"
    exit 1
fi

file_count=$(find "$directory" -type f -name "*.$extension" | wc -l)

echo "$file_count"

