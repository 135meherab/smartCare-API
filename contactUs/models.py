from django.db import models

# Create your models here.
    
class Contact_Us(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=50)
    problem = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'