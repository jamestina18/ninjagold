from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('process-money',views.process_money),
]