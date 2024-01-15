from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=59),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": "wertr",
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,

    
  # custom
  'AUTH_COOKIE': 'access_token',  # Cookie name. Enables cookies if value is set.
  'AUTH_COOKIE_DOMAIN': None,     # A string like "example.com", or None for standard domain cookie.
  'AUTH_COOKIE_SECURE': False,    # Whether the auth cookies should be secure (https:// only).
  'AUTH_COOKIE_HTTP_ONLY' : True, # Http only cookie flag.It's not fetch by javascript.
  'AUTH_COOKIE_PATH': '/',        # The path of the auth cookie.
  'AUTH_COOKIE_SAMESITE': 'Lax',  # Whether to set the flag restricting cookie leaks on cross-site requests. This can be 'Lax', 'Strict', or None to disable the flag
    }

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "account.authenticate.Authentication",
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework_filters.backends.RestFrameworkFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    "LIMIT":10
}


AUTH_USER_MODEL="account.account"
ASGI_APPLICATION="core.asgi.application"

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

INTERNAL_IPS = [
    "127.0.0.1",
]


# DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
# DJANGORESIZED_DEFAULT_SCALE = 0.5
# DJANGORESIZED_DEFAULT_QUALITY = 75
# DJANGORESIZED_DEFAULT_KEEP_META = True
# DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
# DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
# DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True