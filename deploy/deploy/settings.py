from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-x@7=l%*rn%!8t19uoa12_8fdkq5n@qjs#37yfkpfaa_2%y3$qp'
DEBUG = False
ALLOWED_HOSTS = []
INSTALLED_APPS = ['app']
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
