from django.contrib import admin

# Register your models here.
from locator.models import *

admin.site.register(Patroller)
admin.site.register(Shift)
admin.site.register(WatchPoint)
