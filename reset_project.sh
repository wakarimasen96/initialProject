#!/bin/bash
rm db.sqlite3

find . -path "./endpoints/migrations/*.py" -not -name "__init__.py" -delete
find . -path "./endpoints/migrations/*.pyc"  -delete

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username tomasgis --email tomas.gonzalez@urv.cat