from django.contrib import admin
from .models import Designation, Specialisation, AvailableTime, Doctor, Review
# Register your models here.
class AdminDesignationModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

class AdminSpecialisationModel(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}
    
class AdminDoctorModel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation']
    def first_name(self, obj):
        return obj.user.first_name
    def last_name(self, obj):
        return obj.user.last_name
    
class AdminReviewModel(admin.ModelAdmin):
    list_display = ['reviewer', 'doctor']

admin.site.register(Designation, AdminDesignationModel)
admin.site.register(Specialisation, AdminSpecialisationModel)
admin.site.register(Doctor, AdminDoctorModel)
admin.site.register(AvailableTime)
admin.site.register(Review, AdminReviewModel)

