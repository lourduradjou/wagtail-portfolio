import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
application = get_wsgi_application()
User = get_user_model();
User.objects.create_superuser('admin', 'admin@admin.com', 'password')