from django.urls import path

from . import views
from .models import Service

app_name = 'buh'
urlpatterns = [
	path('', views.Index.as_view(), name='index'),
    path('services/', views.Services.as_view(), name='services'),
    path('service_detail/<slug:slug>', views.Service_detail.as_view(), name='service_detail'),
    path('guarantee/', views.Guarantee.as_view(), name='guarantee'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('get_service/', views.GetService.as_view(), name='get_service'),
    path('get_service/<slug:slug>', views.GetService.as_view(), name='get_service'),
    path('get_service/add_service', views.GetService.as_view(), name='add_service'),
	]