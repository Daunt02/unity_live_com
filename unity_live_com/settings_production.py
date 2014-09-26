# -*- coding: utf-8 -*-

import os


# == UTIL ======================================= #

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DIRNAME = os.path.dirname(os.path.abspath(__file__))
_ = lambda s: s


# == DEV ======================================= #

DEBUG = False
TEMPLATE_DEBUG = DEBUG
LOCAL_DEVELOPMENT = False

ALLOWED_HOSTS = [
    'www.jahjah.works',
    'jahjah.works',
    '127.0.0.1'
]


# == ADMIN ======================================= #

ADMINS = (
    ('nerdfiles', 'nerdfiles@gmail.com'),
)
MANAGERS = ADMINS


# == DB ======================================= #

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.join(PROJECT_ROOT, 'prod.sqlite'),
        }
}


# == OTHER ======================================= #

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

INTERNAL_IPS = ('127.0.0.1',)

THEME = 'jahjah'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '_themes', THEME, '_assets')
MEDIA_URL = '/_assets/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, '_themes', THEME, '_templates'),
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, '_themes', THEME, '_assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


MIDDLEWARE_CLASSES = (
    #'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',

    #'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    'jahjah_works.context_processors.date_formats',
    'jahjah_works.context_processors.site_info',
    #'jahjah.context_processors.generic_links',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

ROOT_URLCONF = 'jahjah_works.urls'

WSGI_APPLICATION = 'jahjah_works.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'imagestore',
    'imagestore.imagestore_cms',

    # other
    'social_auth',
    'share',
    'django_social_share',

    # Blog engine
    'fluent_blogs',

    # The content plugins
    'fluent_contents',
    'fluent_contents.plugins.text',

    # Support libs
    'categories',
    'categories.editor',
    'django_wysiwyg',

    # Optional commenting support
    'django.contrib.comments',

    'debug_toolbar',
    'payments',
    'django_forms_bootstrap',
    'django_evolution',
    'menus',
    'mptt',
    'south',
    'djangocms_text_ckeditor',
    'cms',
    'djangocms_picture',
    'djangocms_link',
    'djangocms_file',
    # 'djangocms_snippet', #potential security hazard @see http://docs.django-cms.org/en/latest/getting_started/installation/integrate.html
    'djangocms_googlemap',
    'djangocms_inherit',
    'sekizai',
    'django_extensions',

    'sorl.thumbnail',
    'tagging',
    'mini_charge',
    'generic_links',

    #'filer',
    #'easy_thumbnails',
    #'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    #'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',
    #'cmsplugin_gallery',

    'utils',
    'sqlcipher'

)

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
DJANGO_WYSIWYG_FLAVOR = 'yui_advanced'
FLUENT_BLOGS_BASE_TEMPLATE = 'journal.html'

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

try:
    from .keys import *
except ImportError:
    pass

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.browserid.BrowserIDBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.disqus.DisqusBackend',
    #'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #'social_auth.backends.contrib.github.GithubBackend',
    #'social_auth.backends.contrib.vk.VKOAuth2Backend',
    #'social_auth.backends.contrib.live.LiveBackend',
    #'social_auth.backends.contrib.skyrock.SkyrockBackend',
    #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #'social_auth.backends.contrib.readability.ReadabilityBackend',
    #'social_auth.backends.contrib.fedora.FedoraBackend',
    #'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)


IMAGESTORE_SHOW_USER = False
IMAGESTORE_IMAGE_MODEL = 'mini_charge.models.MiniChargeImage'
# IMAGESTORE_ALBUM_MODEL = 'mini_charge.models.MiniChargeAlbum'
# IMAGESTORE_TEMPLATE = 'base.html'
# IMAGESTORE_LOAD_CSS = True

CMS_TOOLBARS = [
    'cms.cms_toolbar.PlaceholderToolbar',
    'cms.cms_toolbar.BasicToolbar',
    'cms.cms_toolbar.PageToolbar'
]

CMS_TEMPLATES = (
    # core templates
    ('base.html', 'Base Template'),
    ('home.tmpl', 'Home Template'),

    # errors
    ('404.tmpl', 'Template: 404 (not found)'),
    ('500.tmpl', 'Template: 500 (critical error)'),

    # page templates
    ('page.tmpl', 'Page Template'),
    ('page-detail.tmpl', 'Detail Template'),
    ('page-gallery.tmpl', 'Gallery Template'),
    ('page-list.tmpl', 'List Template'),

    # form templates
    ('form.tmpl', 'Form Template'),
    ('form-contact.tmpl', 'Contact Template'),
)


# == SPHINX ======================================= #

THEME = 'jahjah'
THEME_DIR = os.path.join(PROJECT_ROOT, '_themes', THEME)
SPHINX_ROOT = os.path.realpath(os.path.join(THEME_DIR, '_docs', 'html'))
SPHINX_SOURCES_ROOT = os.path.realpath(
    os.path.join(
        THEME_DIR,
        '_docs',
        '_sources'))
SPHINX_ASSETS_ROOT = os.path.realpath(
    os.path.join(
        THEME_DIR,
        '_docs',
        'static'))


# == LOGGING ======================================= #

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        'simple': {
            'format': '%(levelname)s %(message)s'
            },
        },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, '..', '_log', 'requests.log'),
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 10,
            'formatter': 'standard'
            },
        'file_userlogins': {              # define and name a handler
            'level': 'DEBUG',
            # set the logging class to log to a file
            'class': 'logging.FileHandler',
            'formatter': 'verbose',         # define the formatter to associate
            # log file
            'filename': os.path.join(PROJECT_ROOT, '..', '_log', 'userlogins.log')
            },
        'file_usersaves': {               # define and name a second handler
            'level': 'DEBUG',
            # set the logging class to log to a file
            'class': 'logging.FileHandler',
            'formatter': 'verbose',         # define the formatter to associate
            # log file
            'filename': os.path.join(PROJECT_ROOT, '..', '_log', 'usersaves.log')
            },
        },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
            },
        'logview.userlogins': {            # define a logger - give it a name
            # specify what handler to associate
            'handlers': ['file_userlogins'],
            'level': 'INFO',                 # specify the logging level
            'propagate': True,
            },

        'logview.usersaves': {             # define another logger
            'handlers': ['file_usersaves'],  # associate a different handler
            'level': 'INFO',                 # specify the logging level
            'propagate': True,
            },
        }
}

PAYMENTS_PLANS = {
    'monthly': {
        'stripe_plan_id': 'pro-monthly',
        'name': 'Web App Pro ($25/month)',
        'description': 'The monthly subscription plan to WebApp',
        'price': 25,
        'currency': 'usd',
        'interval': 'month'
    },
    'yearly': {
        'stripe_plan_id': 'pro-yearly',
        'name': 'Web App Pro ($199/year)',
        'description': 'The annual subscription plan to WebApp',
        'price': 199,
        'currency': 'usd',
        'interval': 'year'
    },
    'monthly-trial': {
        'stripe_plan_id': 'pro-monthly-trial',
        'name': 'Web App Pro ($25/month with 30 days free)',
        'description': 'The monthly subscription plan to WebApp',
        'price': 25,
        'currency': 'usd',
        'interval': 'month',
        'trial_period_days': 30
    },
}

'''django-share'''
# SHARE_PROVIDERS = {
    #'main': ('facebook', 'twitter', 'pinterest', 'googleplus',),
    #'more': ('email', 'print', ),
#}

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, }


def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar
