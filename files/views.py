from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Product


class FilesCreateView(LoginRequiredMixin, CreateView):
    '''Загрузка файла для конкретного пользователя'''
    model = Product
    fields = ["quantity", "material", "FinishWork", "images", "comments"]

    def form_valid(self, form):
        form.instance.Contractor = self.request.user
        return super().form_valid(form)


# Create your views here.
def calculator(request):
    pass


def myfiles(request):
    pass


def create_files(request):
    pass