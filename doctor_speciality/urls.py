from django.urls import path
from doctor_speciality import views

urlpatterns = [
    path("",views.MyListAPIView.as_view()),
    path("create/", views.MyCreateAPIView.as_view()),
    path("update/<int:pk>/",views.MyUpdateAPIView.as_view()),
    path("delete/<int:pk>/",views.MyDeleteAPIView.as_view())
]