#!/bin/sh
source venv/bin/activate
flask deploy
exec gunicorn -b :5000 --access-logfile - --error-logfile - flask_blog_app:app