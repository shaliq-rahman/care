web: python manage.py collectstatic --noinput --skip-checks && python manage.py migrate --skip-checks && python manage.py sync_permissions_roles && gunicorn config.wsgi:application
