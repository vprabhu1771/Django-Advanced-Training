from django.urls import path
from backend.views import Index, country_check

urlpatterns = [

    path('', Index.as_view()),

    path('ajax/country_check', country_check, name='country_check')

]
