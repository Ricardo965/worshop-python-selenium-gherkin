#!/bin/bash

# Ir al directorio del script
cd "$(dirname "$0")"
source ./venv/bin/activate
cd .
behave >> ./output.txt 2>&1 
deactivate