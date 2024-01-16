from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.
class Specialisation(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.name
    
class Designation(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=30)
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    time = models.CharField(max_length=40)
    def __str__(self):
        return self.time
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    specialisation = models.ManyToManyField(Specialisation)
    designation = models.ForeignKey(Designation, on_delete = models.CASCADE)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet = models.CharField(max_length=100)
    imgage = models.ImageField(upload_to='doctor/images/')

    def __str__(self):
        return f'{self.user.first_name}'


STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')

] 
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    review = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=25, choices = STAR_CHOICES)