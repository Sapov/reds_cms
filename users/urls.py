from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Register, EmailVerify, dashboard, UserListView, UserCreateView, UserUpdateView

# app_name = "users"

urlpatterns = [

    # path('login/', MyLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),

    path(
        'invalid_verify/',
        TemplateView.as_view(template_name='registration/invalid_verify.html'),
        name='invalid_verify'
    ),

    path(
        'verify_email/<uidb64>/<token>/',
        EmailVerify.as_view(),
        name='verify_email',
    ),

    path(
        'confirm_email/',
        TemplateView.as_view(template_name='registration/confirm_email.html'),
        name='confirm_email'
    ),

    path('register/', Register.as_view(), name='register'),
    # ----------------------------CRUD  model USERS-------------------
    path('list_user/', UserListView.as_view(), name='list_users'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<pk>', UserUpdateView.as_view(), name='user_update'),
    # path('user_delete/<pk>', UserDelete.as_view(), name='user_delete'),
]

# <td><a href="{% url 'account:delivery_update' item.id %}">Изменить</a></td>
# <td><a href="{% url 'account:delivery_delete' item.id %}">Удалить</a></td>
