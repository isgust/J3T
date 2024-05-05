import os
from pathlib import Path  # Para manipular caminhos de arquivo de forma segura

# Configuração do diretório base
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta do Django (mantenha em segredo em produção)
SECRET_KEY = 'sua-chave-secreta'

# Modo de depuração (desative em produção)
DEBUG = True

# Hosts permitidos para a execução do projeto (em produção, ajuste isso)
ALLOWED_HOSTS = []

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siteJ3T',  
]

# Middlewares utilizados pelo Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração de URLs
ROOT_URLCONF = 'projeto_j3t.urls'

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pasta global para templates (opcional)
        'APP_DIRS': True,  # Permite ao Django procurar templates nos aplicativos
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

# Configuração WSGI
WSGI_APPLICATION = 'projeto_j3t.wsgi.application'

# Configuração do banco de dados (SQLite neste exemplo)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Use Path para o caminho do banco de dados
    }
}

# Configuração de autenticação
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

# Configuração de idioma
LANGUAGE_CODE = 'pt-br'

# Configuração de fuso horário
TIME_ZONE = 'America/Sao_Paulo'

# Localização
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuração de arquivos estáticos
STATIC_URL = '/static/'

# Opções de cache (opcional)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
