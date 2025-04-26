from django.urls import path

from frontend.views import check_user

urlpatterns = [
    path('check_user', check_user, name='check_user')
]