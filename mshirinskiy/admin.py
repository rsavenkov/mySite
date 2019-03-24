from django.contrib import admin

from .models import *

from mshirinskiy.models import *
from dtemen.models import *

admin.site.register(Question_Mikle)
admin.site.register(Choice_Mikle)
admin.site.register(Act_Mikle)
admin.site.register(dtemenstudent)
admin.site.register(dtemenperson)

# Register your models here.
