from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator as \
    token_generator
from users.forms import UserCreationForm, AuthenticationForm, UserEditForm
from users.models import DeliveryAddress, Organisation
from users.utils import send_email_for_verify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

User = get_user_model()


# class MyLoginView(LoginView):
#     form_class = AuthenticationForm


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('login')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


class UserListView(LoginRequiredMixin, ListView):
    ''' Посмотреть всех юзеров'''
    template_name = "users/user_list.html"
    model = User
    # paginate_by = 5
    # пописать пагинацию в user_list.html


class UserCreateView(LoginRequiredMixin, CreateView):
    '''Добавление нового пользователя'''
    fields = ['email', 'password', 'username', 'first_name', 'last_name', 'phone_number']
    template_name = "users/user_create.html"
    model = User


class UserUpdateView(UpdateView):
    '''Редактирование пользователя'''
    model = User
    # fields = ['username', 'phone_number', 'first_name', 'last_name', 'email', 'is_active', 'email_verify']
    fields = ('__all__')
    template_name_suffix = '_update_form'


class UserDeleteView(LoginRequiredMixin, DeleteView):
    ''' Удаление пользователя  '''
    model = User
    success_url = reverse_lazy('user_list')


def edit_profile(request):
    '''Изменение текущего профиля'''
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
        return render(request, "users/complite_edit.html")
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, "users/edit_profile.html", {"user_form": user_form})


class AddressListView(LoginRequiredMixin, ListView):
    model = DeliveryAddress
    template_name = "users/address_list.html"

    def get_queryset(self):
        "Адреса доставки только этого юзера"
        queryset = DeliveryAddress.objects.filter(user=self.request.user)
        return queryset


class AddressCreateView(LoginRequiredMixin, CreateView):
    '''Добавление нового адреса доставки для пользователя'''
    fields = ['region', 'city', 'street', 'house', 'entrance', 'floor', 'flat', 'first_name', 'second_name',
              'phone', 'delivery_method']
    template_name = "users/address_create.html"
    model = DeliveryAddress

    # только для текущего юзера
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    '''Редактирование адреса доставки для пользователя'''
    model = DeliveryAddress
    fields = ['region', 'city', 'street', 'house', 'entrance', 'floor', 'flat', 'first_name', 'second_name',
              'phone', 'delivery_method']


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    '''Удаление адреса доставки для пользователя'''
    model = DeliveryAddress
    success_url = reverse_lazy('address_list')  # Переходим на страницу списка адресов


class OrganisationListView(LoginRequiredMixin, ListView):
    model = Organisation
    template_name = "users/organisation_list.html"  # Переходим на страницу списка организаций

    def get_queryset(self):
        "Организации  только этого юзера"
        queryset = Organisation.objects.filter(user=self.request.user)
        return queryset


class OrganisationCreateView(LoginRequiredMixin, CreateView):
    '''Добавление новой организации'''
    # fields = ('__all__')
    fields = ['name_ul', 'address_ur', 'address_post', 'phone', 'phone2', 'email', 'inn',
              'kpp', 'okpo']
    model = Organisation
    template_name = "users/organization_create.html"

    # только для текущего юзера
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrganisationUpdateView(LoginRequiredMixin, UpdateView):
    '''редактрование организации'''
    model = Organisation
    fields = ('__all__')
    template_name = "users/organisation_update.html"


class OrganisationDeleteView(LoginRequiredMixin, DeleteView):
    '''Удаление организации'''
    model = Organisation
    success_url = reverse_lazy('organization_list')
