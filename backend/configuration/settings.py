import hashlib
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = hashlib.sha256(os.environ.get("DJANGO_SECRET_KEY").encode()).hexdigest()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "django_celery_beat",
    "waffle",
    "import_export",
    "djangoql",
    "commands",
    "account",
    "myapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "configuration.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "configuration.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_DB_HOST"),
        "PORT": os.environ.get("POSTGRES_DB_PORT"),
        "TEST": {"NAME": f"{os.environ.get('POSTGRES_DB')}_tests"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = os.environ.get("TZ", "UTC")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# authN n authZ
AUTH_USER_MODEL = "account.User"
AUTHENTICATION_BACKENDS = ("account.auth.EmailBackend",)

FRONT_END_PORT = os.environ.get("FRONT_END_PORT", 3000)

CSRF_TRUSTED_ORIGINS = [
    f"http://localhost:{FRONT_END_PORT}",
]


def now_in_us_eat_timezone():
    "Get current time in Africa/Nairobi timezone"
    return datetime.now(ZoneInfo("Africa/Nairobi"))


# ensure shell plus loads all dynamic models as well
# SHELL_PLUS_DONT_LOAD = ['standard', ]
SHELL_PLUS_IMPORTS = [
    "from django.conf import settings",
    "from django.contrib.auth.hashers import make_password",
    "from datetime import datetime, timedelta",
    "from zoneinfo import ZoneInfo",
]

# celery configs
CELERY_BROKER_URL = f"amqp://{os.environ.get('RABBITMQ_DEFAULT_USER')}:{os.environ.get('RABBITMQ_DEFAULT_PASS')}@{os.environ.get('RABBITMQ_HOST')}:5672"
CELERY_TASK_ROUTES = {
    "every_minute_task": {"queue": "quick_asks"},
}

# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#crontab-schedules
CELERY_BEAT_SCHEDULE = {
    "every_minute_task": {
        "task": "every_minute_task",
        "schedule": crontab(
            hour="*", minute="50", nowfun=now_in_us_eat_timezone
        ),  # every hour at 50 minutes past the hour
    },
}
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#using-custom-scheduler-classes
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers.DatabaseScheduler"
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# import export settings
IMPORT_EXPORT_USE_TRANSACTIONS = True
