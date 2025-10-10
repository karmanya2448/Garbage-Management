from django.contrib import admin
from app1.models import *
from models import user_details
# Register your models here.
admin.site.register(user_details)
admin.site.register(driver_info)
admin.site.register(garbageDetails)
admin.site.register(schedule)