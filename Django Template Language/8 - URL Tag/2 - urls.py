from django.urls import path
from frontend.views import about

urlpatterns = [
    path('about/', about, name='about'),
]