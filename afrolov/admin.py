from django.contrib import admin

# Register your models here.

from afrolov.models import *

admin.site.register(Question_afrolov)
admin.site.register(Choice_afrolov)
admin.site.register(Metro)