#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
#deletes obsolete code in multiselect library
sed -i '78,89d' /opt/render/project/src/.venv/lib/python3.11/site-packages/multiselectfield/db/fields.py
