from django.urls import path, include
from files.views import AddFilesUserCreateView, calculator, ViewFilesUserListView, create_files, EditFilesUserUpdateView

app_name = 'files'

urlpatterns = [
    # ------------------CRUD FILE-----------------
    path('load_file/', AddFilesUserCreateView.as_view(), name='load_file'),
    path('', ViewFilesUserListView.as_view(), name='myfiles'),
    path('edit_file/<int:pk>/', EditFilesUserUpdateView.as_view(), name='edit_file'),

    path('calculate/', calculator, name='calculator'),
    path('create_files/', calculator, name='create_files'),

]
