from django.urls import path, include
from files.views import AddFilesUserCreateView, calculator, ViewFilesUserListView, create_files

app_name = 'files'

urlpatterns = [
    # ------------------CRUD FILE-----------------
    path('load_file/', AddFilesUserCreateView.as_view(), name='load_file'),
    path('', ViewFilesUserListView.as_view(), name='myfiles'),

    path('calculate/', calculator, name='calculator'),
    path('create_files/', calculator, name='create_files'),

]
