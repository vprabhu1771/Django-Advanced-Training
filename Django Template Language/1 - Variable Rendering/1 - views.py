from django.shortcuts import render

def show_name(request):
    return render(request, 'frontend/show_name.html', {'name': 'John'})