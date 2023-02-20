from django.contrib import admin
from .models import *

# Register your models here.

#we are telling Django to include the CustomUser/Employee model in the Django Admin site.
#@admin.register(Author)
admin.site.register(CustomUser)
admin.site.register(Employee)

#admin.site.register(Employee)
class UserAdmin(admin.ModelAdmin):
    pass