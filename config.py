import os
from datetime import timedelta
import redis
from urllib.parse import urlparse

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = False
    DEBUG = False
    DEVELOPMENT = False

    USER_APP_NAME = 'PPTX Builder'

    WTF_CSRF_TIME_LIMIT = None

    SESSION_TYPE = 'redis'
    redis_url = os.environ.get("REDIS_URL")
    SESSION_REDIS = redis.from_url(redis_url, ssl=True, ssl_cert_reqs=None)
    SESSION_REFRESH_EACH_REQUEST = True
    REMEMBER_COOKIE_REFRESH_EACH_REQUEST = True
    REMEMBER_COOKIE_DURATION = timedelta(hours=24)
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    CELERY_TASK_RESULT_EXPIRES = os.environ.get('CELERY_TASK_RESULT_EXPIRES', timedelta(minutes=10))

    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION')
    BUCKET = os.environ.get('BUCKET_NAME')
    STORAGE_CLASS = os.environ.get('STORAGE_CLASS')

    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_EMAIL_SENDER_NAME = 'PPTX Builder'
    USER_EMAIL_SENDER_EMAIL = 'info@pptxbuilder.com'

    USER_AFTER_FORGOT_PASSWORD_ENDPOINT = "user.login"
    USER_AFTER_CONFIRM_ENDPOINT = "user.change_password"
    USER_AFTER_CHANGE_PASSWORD_ENDPOINT = "user.login"

    PDF_DOWNLOAD_WAIT_TIME = os.environ.get('PDF_DOWNLOAD_WAIT_TIME', 600)
    PDF_DOWNLOAD_POLLING_PERIOD = os.environ.get('PDF_DOWNLOAD_POLLING_PERIOD', 2)

    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'pptxbuilder', 'assets')
    AWS_S3_UPLOAD = os.path.join(BASE_DIR, 'pptxbuilder', 'assets')

    USER_USER_SESSION_EXPIRATION = 24 * 60 * 60

    PPTX_API_KEY = os.environ.get('PPTX_API_KEY')
    PPTX_API_USERNAME = os.environ.get('PPTX_API_USERNAME')
    PPTX_API_PASSSWORD = os.environ.get('PPTX_API_PASSSWORD')

    REDIS_URL = os.environ.get('REDIS_URL')

    SSE_REDIS_TIMEOUT = os.environ.get('SSE_REDIS_TIMEOUT')

    RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

    SECRET_KEY = os.environ.get('SECRET_KEY', 'VERY-SECRET-K3Y')

    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://postgres:Baj6i6kala@localhost/indigolabs')  # file-based SQL database for dev only
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_DOMAIN_URL = 'http://localhost:5001/'

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'testing-secret-key1')

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY','V1E123RY-SECRDET')