#!/bin/bash

for file in *.py
do
    echo "Running $file..."
    python3 "$file"
    if [ $? -ne 0 ]; then
        exit 1
    fi
done

