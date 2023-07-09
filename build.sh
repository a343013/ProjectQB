#!/usr/bin/env bash

set -o errexit  # exit on error

pip install --upgrade pip

poetry install
poetry self update
poetry lock

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations
