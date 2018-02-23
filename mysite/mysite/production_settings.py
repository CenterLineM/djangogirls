# Import all defalt setting
from .settings import *

import dj_database_url
DATABASE = {
	'default': dj_database_url.config(),
	
}

# Static asset cofiguration.
STATIC_ROOT = 'staticfiles'

# Honor the 'X-forwarded-proto' header for request.is.secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = False