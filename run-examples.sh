#!/bin/bash

set -e

# Iterate over all .py files in the examples directory
for file in examples/*.py; do
  # Run each file with python3
  python3 "$file"
done