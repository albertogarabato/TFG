# settings.py

import os

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Clave secreta para proteger la información sensible
SECRET_KEY = "Trabaj0f1nGrad02o24!"

# Modo de depuración (True para desarrollo, False para producción)
DEBUG = True

# Lista de hosts permitidos para esta aplicación
# ALLOWED_HOSTS = ['cloud.gal', 'localhost', '127.0.0.1', '192.168.247.80']
ALLOWED_HOSTS = ['192.168.247.80', 'localhost', '127.0.0.1']
# Aplicaciones instaladas en el proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'miapp',  # Tus aplicaciones personalizadas aquí
]

# Middleware para procesar las peticiones antes y después de llegar a las vistas
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs principales del proyecto
ROOT_URLCONF = 'CloudIntegrator.urls'

# Configuración de las plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [os.path.join(BASE_DIR, 'miapp/templates/miapp')],
	#'DIRS': [os.path.join(BASE_DIR, 'miapp', 'templates')],
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

# Configuración de la aplicación WSGI
WSGI_APPLICATION = 'CloudIntegrator.wsgi.application'

# Configuración de las bases de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'controlboxcloud': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlboxcloud_db',
        'USER': 'postgres',
        'PASSWORD': 'Infonet',
        'HOST': 'maquiaridos.controlbox.es',
        'PORT': '9343',
    },
    'controlboxcloud2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlboxcloud2_db',
        'USER': 'postgres',
        'PASSWORD': 'Infddonet',
        'HOST': 'ucoga.controlbox.es',
        'PORT': '9343',
    },
    'controlboxcloud3': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlboxcloud3_db',
        'USER': 'softaes',
        'PASSWORD': 'Infddonet',
        'HOST': 'uco.controlbox.es',
        'PORT': '9343',
    },
    'cloudhub': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudhub_db',
        'USER': 'root',
        'PASSWORD': 'Infonet',
        'HOST': 'cloud.infonet.es',
        'PORT': '5443',
    },
    'cloudhub2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudhub2_db',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'HOST': 'cloud.infonet.es',
        'PORT': '6443',
    },
    'cloudhub3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudhub3_db',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'HOST': 'cloud.infonet.es',
        'PORT': '8443',
    },
    'controlboxcloud4': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlboxcloud4_db',
        'USER': 'postgres',
        'PASSWORD': 'Infddonet',
        'HOST': 'example.com',
        'PORT': '5432',
    },
    'controlboxcloud5': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'controlboxcloud5_db',
        'USER': 'postgres',
        'PASSWORD': 'Infddonet',
        'HOST': 'example.com',
        'PORT': '5432',
    },
    'cloudhub4': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudhub4_db',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'HOST': 'example.com',
        'PORT': '3306',
    },
    'cloudhub5': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cloudhub5_db',
        'USER': 'root',
        'PASSWORD': 'Infonddet',
        'HOST': 'example.com',
        'PORT': '3306',
    },
}

# Routers de bases de datos
DATABASE_ROUTERS = ['miapp.routers.DatabaseRouter']

# Configuración de validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.UppercaseValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.SymbolValidator',
    },
]


# Configuración del idioma
LANGUAGE_CODE = 'en-us'

# Zona horaria del proyecto
TIME_ZONE = 'UTC'

# Configuración de uso de idioma
USE_I18N = True

# Configuración de uso de zona horaria
USE_L10N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Campo automático predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
