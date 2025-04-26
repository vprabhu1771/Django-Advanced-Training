from django.shortcuts import render

def check_user(request):
    return render(request, 'frontend/check_user.html', {'is_logged_in': True})