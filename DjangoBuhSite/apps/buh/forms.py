from django.forms import ModelForm

from .models import ServiceRequest

class ServiceForm(ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('name', 'phone', 'email', 'service', 'description')