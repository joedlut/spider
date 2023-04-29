from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=15ed40817386f8ba6a90120519cad5e9a10fbc1ea789523e475107a7f12f02df"
DEBUG = True

ALLOWED_HOSTS = ['localhost']



sentry_sdk.init(
    dsn="http://2614f94a3f7047cc818b865865c3df41@192.168.88.133:9000/2",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

