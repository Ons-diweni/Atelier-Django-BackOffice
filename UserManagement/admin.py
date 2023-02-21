from django.contrib import admin
from .models import *

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    verbose_name  = 'Users'
    date_hierarchy = 'date_joined'
    empty_value_display = '-empty-'
    #If you want a form for the CustomUser model that includes only the first_name , last_name and email fields, you would specify fields like this:
    fields = ('first_name', 'last_name' , 'email' , 'password')
    
class EmployeeAdmin(admin.ModelAdmin):
    verbose_name  = 'Employees'    
    
 
    
#we are telling Django to include the CustomUser and  the Employee models in the Django Admin site.
#@admin.register(Author)
admin.site.register(CustomUser , CustomUserAdmin)
admin.site.register(Employee , EmployeeAdmin)