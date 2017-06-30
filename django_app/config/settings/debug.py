# debug.py
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']
