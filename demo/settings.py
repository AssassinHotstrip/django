"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# 导入操作系统模块
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 项目根路径
# /home/python/PythonLearn/Django/demo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# django默认秘钥
SECRET_KEY = 'a*j039ba)2o3-xq13v5z)7zi9s#4)=-$#oge7z5q@+o=mp%1dr'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认开启调试模式，部署上线后需关闭
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 安装自己创建的子应用，及安装第三方子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users.apps.UsersConfig', #安装users子应用
    'request_response.apps.RequestResponseConfig',
    'class_view.apps.ClassViewConfig',

]

# 中间件，类似flask中的请求勾子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.my_middleware',  # 自定义中间件
    'middleware.my_middleware2',  # 自定义中间件
]

# 项目的路由入口
ROOT_URLCONF = 'demo.urls'

# 模板文件配置项
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 配置静态文件路径
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

# 部署上线后程序入口
WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# 数据库配置项，默认为sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# 验证密码规则
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 本地化语言，默认英文'en-us'， 可改成中文zh-Hans
LANGUAGE_CODE = 'en-us'

# 时区，默认世界时间， 可改成亚洲/上海 ‘Asia/Shanghai’
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
# 默认静态文件访问前缀
STATIC_URL = '/static/'

# 注意：只有开启调试模式的时候，才能提供静态文件访问功能，关闭调试模式后静态文件无法访问
# Django是一个动态业务逻辑框架，不擅长静态文件访问， 需要访问时利用nginx服务器
# 查找静态文件的目录
STATICFILES_DIRS  = [
    # 指定静态文件的访问路径
    os.path.join(BASE_DIR, 'static_files'),
    # 若上面的匹配不成功，则匹配该路径
    os.path.join(BASE_DIR, 'static_files/image'),
]


# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        #                        自己的ip地址/redis数据库编号
        "LOCATION": "redis://192.168.14.117/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"