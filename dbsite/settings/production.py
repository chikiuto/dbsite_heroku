from .base import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dbsite-heroku.herokuapp.com','.herokuapp.com','127.0.0.1']

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)