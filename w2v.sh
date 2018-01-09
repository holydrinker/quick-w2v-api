#!/usr/bin/env bash
source env/bin/activate
export FLASK_APP=w2v.py
python -m flask run
