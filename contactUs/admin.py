from django.contrib import admin
from .models import Contact_Us
# Register your models here.
class AdminContactModel(admin.ModelAdmin):
    list_display = ['name', 'phone', 'subject']

admin.site.register(Contact_Us,AdminContactModel)