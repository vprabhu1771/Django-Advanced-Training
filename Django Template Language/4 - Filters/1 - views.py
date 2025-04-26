from django.shortcuts import render

def show_user(request):
    return render(request, 'frontend/show_user.html', {'username': 'john doe'})