#!/bin/bash

# Check if the file name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

FILENAME=$1

# Find the file in the current directory or any subdirectory
FILEPATH=$(find . -name "$FILENAME" -print -quit)

# Check if the file was found
if [ -z "$FILEPATH" ]; then
    echo "File $FILENAME not found"
    exit 1
fi

# Run the Python file
python3 "$FILEPATH"

