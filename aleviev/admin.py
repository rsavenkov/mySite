from django.contrib import admin

from .models import Street
from .models import House

admin.site.register(Street)
admin.site.register(House)
