web: gunicorn --bind 0.0.0.0:$PORT --workers 1 server:app
web: python "mio_bot.py" bundle exec rails s -p $PORT

