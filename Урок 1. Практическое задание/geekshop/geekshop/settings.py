"""
Django settings for geekshop project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Базовая директория, где находится проект
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&3tne&^pa0sbd7(*l!r3*b8y8njd2!o-wuy!v^xo^t!$q2!ppv'

# SECURITY WARNING: don't run with debug turned on in production!
# Если DEBUG = True - то отображается вся информация об отладке
# Если DEBUG = False - то отображается стандартная страничка с ошибкой (например "Error 404")
DEBUG = True

# Указывается доменное имя хостинга
ALLOWED_HOSTS = []


# Application definition
# Установленные приложения

INSTALLED_APPS = [
    'django.contrib.admin',         # Админка
    'django.contrib.auth',          # Модуль авторизации
    'django.contrib.contenttypes',  # Контенты
    'django.contrib.sessions',      # Сессии
    'django.contrib.messages',      # Сообщения
    'django.contrib.staticfiles',   # Работа со статикой
    'mainapp',
    'authapp',
    'basketapp',
    'adminapp',
]

# Прослойки
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный файл конфигурации "урлов"
ROOT_URLCONF = 'geekshop.urls'

# Шаблоны (это непосредственно html странички, которые будут преобразовываться "вьюшками" для отображения данных)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainapp.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'geekshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# Базы данных
# Параметр ENGINE указывает на используемый движок для доступа к БД
# NAME указывает на путь к базе данных

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',         # Драйвер подключения
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),   # Название БД
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# Раздел по поводу валидаторов авторизации

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# Язык, который будет использоваться
LANGUAGE_CODE = 'ru'

# Тайм зона
TIME_ZONE = 'UTC'

# Включить переводы
USE_I18N = True

USE_L10N = True

# Тайм зоны
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# Статик файлы

# STATIC_URL — это путь по сети (доступ из браузера)
STATIC_URL = '/static/'

# STATICFILES_DIRS — это пути к статическим файлам на жестком диске (доступ из файловой системы)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# это media относящиеся к каким-то личным картинкам или пользовательским действиям
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Это необходимо, чтобы Django вместо модели User использовал в приложении аутентификации нашу модель
AUTH_USER_MODEL = 'authapp.ShopUser'

LOGIN_URL = '/auth/login/'

DOMAIN_NAME = 'http://localhost:8000'

EMAIL_HOST = 'localhost'    # URL адрес почтового сервера
EMAIL_PORT = '25'           # порт сервера
EMAIL_HOST_USER = 'django@geekshop.local'   # имя пользователя, от которого будет отправлена почта (закоментить для вар №1)
EMAIL_HOST_PASSWORD = 'geekshop'    # пароль пользователя, от которого будет отправлена почта (закоментить для вар №1)
EMAIL_USE_SSL = False       # флаг использования шифрования

#вариант №1 python -m smtpd -n -c DebuggingServer localhost:25
# EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = None, None

#вариант №2 логирования сообщений почты в виде файлов вместо отправки
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

# Для Яндекса
# # чтобы приходили отчёты об ошибках
# ADMINS = (
#     ('Oleg', 'this_is@my.email'),
# )
# MANAGERS = ADMINS
#
#
# # настройки почтового сервера (почтового отправителя)
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_PASSWORD = 'password'
# EMAIL_HOST_USER = 'noerply@mydomain.com'
# EMAIL_PORT = '465'
# EMAIL_USE_SSL = True
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
