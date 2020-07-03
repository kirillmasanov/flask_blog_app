Blog Application (built with [Flask](https://github.com/pallets/flask/))
===================================
This application was developed while studying the book [Flask Web Development: Developing Web Applications with Python, 2nd Edition](https://www.amazon.com/Flask-Web-Development-Developing-Applications/dp/1491991739/ref=sr_1_1?crid=4W0R9JWWYHFZ&dchild=1&keywords=flask+web+development&qid=1593712495&sprefix=flask+web%2Caps%2C357&sr=8-1) by [Miguel Grinberg](https://github.com/miguelgrinberg/flasky).

##### The list of used technologies and implemented functions:
- Using the database:

  * *[SQLLite](https://www.sqlite.org/index.html)* (for dev server) with *[Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy/)*
  * Database Migrations with *[Flask-Migrate](https://github.com/miguelgrinberg/flask-migrate)*
- User authentication system:
  * *[Flask-Login](https://github.com/maxcountryman/flask-login)*: Management of user sessions for logged-in users
  * *[Werkzeug](https://github.com/pallets/werkzeug)*: Password hashing and verification
  * *[itsdangerous](https://github.com/pallets/itsdangerous)*: Cryptographically secure token generation and
verification
- User roles and permissions (admin panel, moderation)
- User profile pages
- The blogging interface:
  * [Bootstrap-Flask](https://github.com/greyli/bootstrap-flask): HTML templates
  * [Flask-WTF](https://github.com/lepture/flask-wtf): Web forms
  * [Jinja](https://github.com/pallets/jinja/): templating engine
- Followers
- User comments for blog posts
- Pagination with [Bootstrap-Flask](https://github.com/greyli/bootstrap-flask)
- User avatars (provided by [Gravatar](https://en.gravatar.com/site/implement/images/python/))
- Rich-Text Posts with *[Markdown](https://python-markdown.github.io/)*, *[Bleach](https://github.com/mozilla/bleach)* and *[Flask-PageDown](https://github.com/miguelgrinberg/Flask-PageDown)*
- Email support with *[Flask-Mail](https://github.com/mattupstate/flask-mail)*, sending of authentication-related emails
- An application programming interface (API)
- Testing: Unit tests, [HTTPie](https://github.com/jakubroztocil/httpie#python-version), [Coverage](https://github.com/nedbat/coveragepy/blob/coverage-5.1/doc/index.rst), end-to-end testing with [Selenium](https://selenium-python.readthedocs.io/). Creating Fake Blog Post Data with [Faker](https://github.com/joke2k/faker)
- Deployment: [Heroku](https://heroku.com/), with [Docker Containers](https://www.docker.com/) and traditional deployments 
