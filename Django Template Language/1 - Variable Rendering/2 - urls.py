from django.urls import path

from frontend.views import show_name

urlpatterns = [
    path('show_name', show_name, name='show_name')
]