from django.contrib import admin
from .models import *

# Register your models here.


#here we tell the admin that UserApp and Employe objects have an admin interface.
admin.site.register(CustomUser)
#admin.site.register(Employee)
class UserAdmin(admin.ModelAdmin):
    pass