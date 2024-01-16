from typing import Any
from django.contrib import admin
from .models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.
class AdminAppointmentModel(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_type', 'appointment_status', 'time', 'cancel']

    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    
    def patient_name(self, obj):
        return obj.patient.user.first_name
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == 'running' and obj.appointment_type =='Online':
            email_subject = 'Appointment in Running'
            email_body = render_to_string('appointment_mail.html',{'user': obj.patient.user, 'doctor': obj.doctor,})
            email = EmailMultiAlternatives(email_subject, '', to = [obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
    
admin.site.register(Appointment, AdminAppointmentModel)