from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from doctor_speciality.serializers import DoctorSpecialitySerializer
from doctor_speciality.models import Speciality

# Create your views here.
class MyListAPIView(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = DoctorSpecialitySerializer

class MyCreateAPIView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = DoctorSpecialitySerializer

class MyUpdateAPIView(UpdateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = DoctorSpecialitySerializer

class MyDeleteAPIView(DestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class = DoctorSpecialitySerializer
