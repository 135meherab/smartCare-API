from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
# Create your models here.

APPOINTMENT_TYPE = [
    ('Offline','Offline'),
    ('Online','Online'),
]
APPOINTMENT_STATUS = [
    ('pending','pending'),
    ('running','running'),
    ('complete','complete'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    appointment_type = models.CharField(max_length=25, choices = APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=25, choices = APPOINTMENT_STATUS, default = 'pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE)
    cancel = models.BooleanField(default=False)