from rest_framework import serializers
from . models import Appointment
# Create your tests here.

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many = False)
    doctor = serializers.StringRelatedField(many = False)
    patient = serializers.StringRelatedField(many = False)
    class Meta:
        model = Appointment
        fields = '__all__'