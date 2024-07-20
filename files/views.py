from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView

from .models import Product


class AddFilesUserCreateView(LoginRequiredMixin, CreateView):
    '''Create a new file'''
    model = Product
    fields = ["quantity", "material", "FinishWork", "images", "comments"]

    def form_valid(self, form):
        form.instance.Contractor = self.request.user
        return super().form_valid(form)


class ViewFilesUserListView(LoginRequiredMixin, ListView):
    """Посмотреть все файлы пользователя"""

    model = Product
    paginate_by = 5
    template_name = "files/view_product.html"
    login_url = "login"

    def get_queryset(self):
        queryset = Product.objects.filter(Contractor=self.request.user).order_by("-id")
        return queryset


class EditFilesUserUpdateView(LoginRequiredMixin, UpdateView):
    '''Редактирование файла пользователя'''
    model = Product
    fields = ["quantity", "material", "FinishWork"]
    template_name = "files/product_update_form.html"
    login_url = "login"


def calculator(request): pass


def myfiles(request): pass


def create_files(request): pass
