from .base import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dbsite-heroku.herokuapp.com', '*']

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)