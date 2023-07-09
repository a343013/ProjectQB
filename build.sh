#!/usr/bin/env bash

set -o errexit  # exit on error

/opt/render/project/src/.venv/bin/python -m pip install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
