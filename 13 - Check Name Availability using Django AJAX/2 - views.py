from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from backend.models import Country

class Index(CreateView):
    model = Country

    fields = '__all__'

    template_name = "backend/index.html"

def country_check(request):

    if request.method == 'POST' and request.POST.get('search_country') != '':
        country_response = Country.objects.filter(name__icontains=request.POST.get('search_country'))
        if country_response:
            errno_template = "<span style='color: red;'>{} already exists</span>".format(request.POST.get('search_country'))

            return HttpResponse(errno_template)

        else:
            success_template = "<span style='color: green;'>{} available</span>".format(request.POST.get('search_country'))
            return HttpResponse(success_template)