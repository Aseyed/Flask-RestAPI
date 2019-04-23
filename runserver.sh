#!/bin/bash
#pipenv shell
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host 127.0.0.1 --port 5050
