from django.urls import path, include
from files.views import FilesCreateView, calculator, myfiles, create_files

app_name = 'files'

urlpatterns = [
    # ------------------CRUD FILE-----------------
    path('load_file/', FilesCreateView.as_view(), name='load_file'),

    path('calculate/', calculator, name='calculator'),
    path('myfiles/', calculator, name='myfiles'),
    path('create_files/', calculator, name='create_files'),

]
