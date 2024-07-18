from django.urls import path, include
from django.views.generic import TemplateView

from users.views import Register, EmailVerify, dashboard, UserListView, UserCreateView, UserUpdateView, UserDeleteView, \
    edit_profile, AddressListView, AddressCreateView, AddressUpdateView, AddressDeleteView, OrganisationListView, \
    OrganisationCreateView, OrganisationUpdateView, OrganisationDeleteView

urlpatterns = [
    # ------------------------AUTH------------------
    path('', include('django.contrib.auth.urls')),
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),
    path('register/', Register.as_view(), name='register'),
    # ----------------------------CRUD  model USERS-------------------
    path('list_user/', UserListView.as_view(), name='user_list'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_update/<pk>', UserUpdateView.as_view(), name='user_update'),
    path('user_delete/<pk>', UserDeleteView.as_view(), name='user_delete'),
    # -------------------------EDIT PROFILE USER-------------------
    path('edit_profile', edit_profile, name='edit_profile'),
    # -----------------CRUD ADDRESS DELIVERY---------------------
    path('list_address/', AddressListView.as_view(), name='address_list'),
    path('create_address/', AddressCreateView.as_view(), name='address_create'),
    path('update_address/<pk>', AddressUpdateView.as_view(), name='address_update'),
    path('delete_address/<pk>', AddressDeleteView.as_view(), name='address_delete'),
    # ---------------------CRUD ORGANISATION---------------------
    path('list_organization/', OrganisationListView.as_view(), name='list_organization'),
    path('create_organisation/', OrganisationCreateView.as_view(), name='create_organisation'),
    path('update_organisation/<pk>', OrganisationUpdateView.as_view(), name='update_organisation'),
    path('delete_organisation/<pk>', OrganisationDeleteView.as_view(), name='delete_organisation'),


]
