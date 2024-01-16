from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from .models import Doctor, AvailableTime, Designation, Specialisation, Review
from .serializars import DoctorSerializer, DesignationSerializer, SpecialisationSerializer, ReviewSerializer, AvailableTimeSerializer

# Create your views here.


class DoctorPagePagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagePagination


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class SpecialisationViewSet(viewsets.ModelViewSet):
    queryset = Specialisation.objects.all()
    serializer_class = SpecialisationSerializer

class DoctorBaseAvailableTime(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [DoctorBaseAvailableTime]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer