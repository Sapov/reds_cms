from django.urls import path, include
from files.views import AddFilesUserCreateView, calculator, ViewFilesUserListView, \
    EditFilesUserUpdateView, DeleteFilesUserDeleteView, FilesCreateViewInter, FilesCreateViewLarge, FilesCreateViewUV

app_name = 'files'

urlpatterns = [
    # ---------------------------------CRUD FILE---------------------------------
    path('load_file/', AddFilesUserCreateView.as_view(), name='load_file'),
    path('load_file_inter/', FilesCreateViewInter.as_view(), name='create_inter'),
    path('load_file_large/', FilesCreateViewLarge.as_view(), name='create_large'),
    path("create_uv/", FilesCreateViewUV.as_view(), name="create_uv"),
    # path("create_rollup/", FilesCreateViewRollUp.as_view(), name="create_rollup"),

    path('', ViewFilesUserListView.as_view(), name='myfiles'),
    path('edit_file/<int:pk>/', EditFilesUserUpdateView.as_view(), name='edit_file'),
    path('delete_file/<int:pk>/', DeleteFilesUserDeleteView.as_view(), name='delete_file'),

    path('calculate/', calculator, name='calculator'),
    path('create_files/', calculator, name='create_files'),

]