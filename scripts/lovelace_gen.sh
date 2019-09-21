#!/bin/bash

cd "/home/homeassistant/.homeassistant/" || exit
python3 python_scripts/lovelace-gen.py
