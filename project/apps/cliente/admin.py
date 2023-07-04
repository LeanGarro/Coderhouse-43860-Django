from django.contrib import admin
from django.db import models

from .models import models

admin.site.register(models)
admin.site.register(models.user)
