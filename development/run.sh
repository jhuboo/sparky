#!/bin/bash

cd ~/spotmicroai || exit
export PYHONPATH=.

venv/bin/python3

development/runtime/script.py
