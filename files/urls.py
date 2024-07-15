from django.urls import path, include
from files.views import calculator

app_name = 'files'

urlpatterns = [
    path('calculator/', calculator, name='calculator'),
]
