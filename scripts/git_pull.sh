#!/bin/bash

cd "/home/homeassistant/.homeassistant/" || exit
git checkout master
git pull
python3 python_scripts/lovelace-gen.py
