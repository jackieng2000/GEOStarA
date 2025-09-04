import os
from pathlib import Path
from django.contrib.messages import constants as messages
from datetime import timedelta
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# OAuth Configuration (make sure these environment variables are set)
GOOGLE_OAUTH2_CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID', default='')
GOOGLE_OAUTH2_SECRET = config('GOOGLE_OAUTH2_SECRET', default='')
GITHUB_OAUTH2_CLIENT_ID = config('GITHUB_OAUTH2_CLIENT_ID', default='')
GITHUB_OAUTH2_SECRET = config('GITHUB_OAUTH2_SECRET', default='')

# Quick-start development settings - unsuitable for production
SECRET_KEY = config('SECRET_KEY', default='django-insecure-fallback-key-for-dev')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['209.97.164.73', 'jackieng.hk','127.0.0.1',
 'localhost','backend.jackieng.hk', 'test.jackieng.hk']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    'gpsinfo',
    'accounts',
    'api',
    'pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# REST Framework Configuration (only once)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT Configuration (only once)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,
}

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "http://localhost:8000",
    "http://209.97.164.73:5173",
    "http://localhost:5173",
    "https://jackieng.hk",
    "https://www.jackieng.hk",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'rbackend.urls'

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

WSGI_APPLICATION = 'rbackend.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='geoinf_db'),
        'USER': config('DB_USER', default='dbadmin'),
        'PASSWORD': config('DB_PASSWORD', default='1234'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default=''),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # Commented out for development
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Hong_Kong'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'rbackend/static'),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django Allauth Configuration
SITE_ID = 1

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth settings
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True

# Social account settings
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True

# Social OAuth providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
    },
    'github': {
        'SCOPE': ['user:email'],
    }
}

# Login/Logout URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'pages:index'  # Redirect to your index page after login
LOGOUT_REDIRECT_URL = 'pages:index'


ACCOUNT_LOGOUT_REDIRECT_URL = 'pages:index'  # Redirect to index after logout

# Optional: Customize the login URL if needed
#LOGIN_URL = 'account_login'


# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# If you're having issues with the decouple config, create a .env file:
# Create a file named .env in your project root with:
# SECRET_KEY=your-real-secret-key-here
# DEBUG=True
# DB_NAME=geoinf_db
# DB_USER=dbadmin
# DB_PASSWORD=1234
# DB_HOST=localhost
# GOOGLE_OAUTH2_CLIENT_ID=your-google-client-id
# GOOGLE_OAUTH2_SECRET=your-google-secret
# GITHUB_OAUTH2_CLIENT_ID=your-github-client-id
# GITHUB_OAUTH2_SECRET=your-github-secret