from django.urls import path
from . import views

urlpatterns = [
    path('judge_test/', views.judge_test, name='judge_test'),
]