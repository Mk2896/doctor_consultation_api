web: gunicorn docter_consultation_app.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py makemigrations
manage.py migrate