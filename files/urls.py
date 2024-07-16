from django.urls import path, include
from files.views import calculator, myfiles, create_files

app_name = 'files'

urlpatterns = [
    path('calculator/', calculator, name='calculator'),
    path('create_files/', create_files, name='create_files'),
    path('myfiles/', myfiles, name='myfiles'),
]
