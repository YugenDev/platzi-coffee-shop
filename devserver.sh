#!/bin/sh
source .venv/bin/activate
python coffee_shop/manage.py runserver $PORT
