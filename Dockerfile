FROM python:3.6-alpine

ENV FLASK_APP flask_blog_app.py
ENV FLASK_CONFIG production

RUN adduser -D flask_blog_app
USER flask_blog_app

WORKDIR /home/flask_blog_app

COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY flask_blog_app.py config.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]