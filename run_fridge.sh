#!/bin/bash

# Checks for Python 3 then 2 and runs what is available

if command -v python3 >/dev/null 2>&1; then
  python3 fridge.py
else
  if command -v python >/dev/null 2>&1; then
    python fridge.py
  else
    echo "Error: Python 3 or Python 2 is required to run this script"
  fi
fi
