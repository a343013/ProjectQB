#!/usr/bin/env bash

set -o errexit  # exit on error

pip install --upgrade pip

poetry install
poetry self update
poetry lock
# Instalar la versión deseada de Python
pyenv install 3.10.6

# Establecer la versión de Python como global
pyenv global 3.10.6

# Continuar con otros comandos de construcción


pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations
