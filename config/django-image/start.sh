#!/bin/bash

set -e

cd /app

# Crear proyecto Django si no existe
if [ ! -f manage.py ]; then
    django-admin startproject backend .
fi

# Migraciones
python manage.py makemigrations || true
python manage.py migrate

# Crear superusuario automáticamente (si no existe)
python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()

username = "${DJANGO_SUPERUSER_USERNAME}"
email = "${DJANGO_SUPERUSER_EMAIL}"
password = "${DJANGO_SUPERUSER_PASSWORD}"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
EOF

# Levantar servidor
python manage.py runserver 0.0.0.0:8000
