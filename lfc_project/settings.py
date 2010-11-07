# coding:utf-8
import os
DIRNAME = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('name', 'email'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'curtocircuito.db'      # Or path to database file if using sqlite3.
DATABASE_USER = ''         # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = DIRNAME + "/media"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    "pagination.middleware.PaginationMiddleware",
    "lfc.utils.middleware.LFCMiddleware",
)

CACHE_MIDDLEWARE_KEY_PREFIX = "lfc"
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    "lfc_theme",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    "django.contrib.flatpages",
    "django.contrib.sitemaps",
    "django.contrib.comments",
    "lfc",
    "portlets",
    "tagging",
    "contact_form",
    "pagination",
    "workflows",
    "permissions",
    "lfc_blog",
)

CACHE_BACKEND = 'dummy:///'

FORCE_SCRIPT_NAME=""
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'lfc.context_processors.main',
)


DEFAULT_FROM_EMAIL = ""
EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PAGINATION_DEFAULT_PAGINATION = 5
PAGINATION_DEFAULT_WINDOW = 1

LANGUAGES = (("en", u"English"), ("de", u"German"), ("pt-BR","Portuguese"))
LFC_MULTILANGUAGE = len(LANGUAGES) > 1
LFC_MANAGE_WORKFLOWS = True
LFC_MANAGE_PERMISSIONS = True
LFC_MANAGE_APPLICATIONS = True
LFC_MANAGE_USERS = True

#permite fazer configuraçoes locais
try:
    execfile(PROJECT_PATH+'/local_settings.py')
    #print 'Usando configuracao LOCAL'
except IOError:
    #print 'Usando configuracao PADRAO'
    pass

