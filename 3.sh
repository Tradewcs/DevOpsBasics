#!/bin/bash

directory=""
text=""

usage() {
    echo "usage: $0 -p <path> -s <text>"
    exit 1
}

while getopts "p:s:" opt; do
  case $opt in
    p) directory=$OPTARG ;;
    s) text=$OPTARG ;;
    *) usage ;;
  esac
done

if [ -z "$directory" ] || [ -z "$text" ]; then
    usage
fi

if [ ! -d "$directory" ]; then
    echo "Directory $directory does not exists"
    exit 1
fi

grep -rl "$text" "$directory"

