from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_Us
from .serializers import ContactUsSerializer
class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = Contact_Us.objects.all()
    serializer_class = ContactUsSerializer