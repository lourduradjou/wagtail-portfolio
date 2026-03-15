import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.dev")
application = get_wsgi_application()


# User = get_user_model()

# username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
# email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
# password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

# if not username or not email or not password:
#     raise ValueError("Superuser credentials not provided")

# if not User.objects.filter(username=username).exists():
#     print("Creating superuser...")
#     User.objects.create_superuser(
#         username=username,
#         email=email,
#         password=password
#     )
# else:
#     print("Superuser already exists")