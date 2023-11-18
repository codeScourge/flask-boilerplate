cd api
gunicorn -c config.py app:app
