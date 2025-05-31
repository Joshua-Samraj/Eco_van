#!/usr/bin/env bash
# install dependencies and run collectstatic
pip install -r requirements.txt
python manage.py collectstatic --noinput
