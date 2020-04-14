from django.urls import reverse
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponseRedirect

from . import models
from . import forms


class Index(View):
    def get(self, request):
        return render(request, 'buh/index.html')


class Services(View):
    def get(self, request):
        services = models.Service.objects.filter(publish=True)
        return render(request, 'buh/services.html', {'services': services})
    

class Service_detail(View):
    def get(self, request, slug):
        service = models.Service.objects.get(url=slug)
        return render(request, 'buh/service_detail.html', {'service': service})


class Guarantee(View):
    def get(self, request):
        return render(request, 'buh/guarantee.html')


class Contacts(View):
    def get(self, request):
        return render(request, 'buh/contacts.html')


class GetService(View):
    def get(self, request, slug=None):
        services = models.Service.objects.filter(publish=True)
        args = [request, 'buh/get_service.html', {'services': services}]
        if slug is not None:
            service = models.Service.objects.get(url=slug)
            args[2]['service'] = service
        return render(*args)

    def post(self, request, slug):
        service = models.Service.objects.get(title=request.POST['service'])
        data = request.POST.copy()
        data['service'] = service
        form = forms.ServiceForm(data)
        if form.is_valid():
            form = form.save()

        slug = service.url
        return HttpResponseRedirect(reverse('buh:service_detail', args=(slug,)))