from django.urls import path
from estudiantes import views

urlpatterns = [
    path('', views.StudentView.as_view()),
]
