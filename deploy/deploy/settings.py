from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = lambda base: os.path.abspath(os.path.join(os.path.dirname(__file__), '../', base).replace('\\', '/'))
SECRET_KEY = 'django-insecure-x@7=l%*rn%!8t19uoa12_8fdkq5n@qjs#37yfkpfaa_2%y3$qp'
DEBUG = False
STATIC_ROOT = PROJECT_DIR('static')
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
    os.path.join(BASE_DIR, 'my24frontend', 'dist'),
)

ALLOWED_HOSTS = []
INSTALLED_APPS = ['app', 'django.contrib.staticfiles']
MIDDLEWARE = []
ROOT_URLCONF = 'deploy.urls'
TEMPLATES = []
DATABASES = {}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LINODE_S3_BUCKET_DEV_DEPLOYMENTS = 'dev-deployments'
LINODE_S3_BUCKET_LIVE_DEPLOYMENTS = 'live-deployments'
LINODE_ENDPOINT_URL_DEV_DEPLOYMENTS = 'dev-deployments.eu-central-1.linodeobjects.com'
LINODE_ENDPOINT_URL_LIVE_DEPLOYMENTS = 'live-deployments.eu-central-1.linodeobjects.com'
