from rest_framework import serializers
from doctor_speciality.models import Speciality

class DoctorSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = "__all__"