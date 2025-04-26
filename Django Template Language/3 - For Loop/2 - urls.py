from django.urls import path

from frontend.views import list_fruits

urlpatterns = [
    path('list_fruits', list_fruits, name='list_fruits')
]