from django.urls import path

from frontend.views import show_user

urlpatterns = [
    path('show_user', show_user, name='show_user')
]