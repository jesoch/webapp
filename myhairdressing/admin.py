from django.contrib import admin
from .models import Hairdressing, Schedule, Citation

# Register your models here.

admin.site.register(Hairdressing)
admin.site.register(Schedule)
admin.site.register(Citation)