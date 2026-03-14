import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
application = get_wsgi_application()

from mysite.utils.create_superuser import create_superuser
create_superuser()