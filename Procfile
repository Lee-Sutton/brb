web: gunicorn config.wsgi:application
worker: celery worker --app=brb.taskapp --loglevel=info
