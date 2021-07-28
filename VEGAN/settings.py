
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm4y19q)3rp)$d-0qp(r)iht!el7&=r2p57zdpk_$3z&ecz2i7+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third party
    'rest_framework',
    'django_render_partial',

    #API CUSTOM APPS
    'VEGAN_API.VEGAN_API_ACCOUNT',
    'VEGAN_API.VEGAN_API_CART',
    'VEGAN_API.VEGAN_API_CATEGORY',
    'VEGAN_API.VEGAN_API_COMMENT',
    'VEGAN_API.VEGAN_API_GALLERY',
    'VEGAN_API.VEGAN_API_PRODUCT',
    'VEGAN_API.VEGAN_API_PRODUCT_GALLERY',
    'VEGAN_API.VEGAN_API_SEARCH',
    'VEGAN_API.VEGAN_API_SITE',
    'VEGAN_API.VEGAN_API_TAG',
    'VEGAN_API.VEGAN_API_BRAND',
    'VEGAN_API.VEGAN_API_BLOG',
    'VEGAN_API.VEGAN_API_CHECKOUT',

    # render parital app encapsulates all partially renderd templates
    'VEGAN_PARTIAL'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VEGAN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'VEGAN.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL  = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'storage', 'STATIC')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]

MEDIA_URL  = '/user/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage', 'MEDIA')

AUTH_USER_MODEL = 'VEGAN_API_ACCOUNT.User'

LOGIN_URL = '/account/'