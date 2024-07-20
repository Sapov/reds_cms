from django import forms

from files.models import Material, Product
from .models import *


class UploadFilesInter(forms.ModelForm):
    """Форма загрузки файлов для интерьерной печати отфильтруем только интерьерную печать"""

    material = forms.ModelChoiceField(
        queryset=Material.objects.filter(type_print=2),
        label="Выберите материал для печати",
        initial=13,  # по умолчанию пленка матовая Китай
    )

    class Meta:
        model = Product
        fields = [
            "quantity",
            "material",
            "FinishWork",
            "images",
            "comments"
        ]


class UploadFilesLarge(forms.ModelForm):
    """Форма загрузки файлов для Широкоформатной печати отфильтруем только широкоформатную печать"""

    material = forms.ModelChoiceField(
        queryset=Material.objects.filter(type_print=1),
        label="Выберите материал для печати",
        initial=1,  # по умолчанию 440 баннер
    )

    class Meta:
        model = Product
        fields = ["quantity", "material", "FinishWork", "images", "comments"]


class UploadFilesUV(forms.ModelForm):
    """Форма загрузки файлов для UV-печати отфильтруем только UV-печать"""

    material = forms.ModelChoiceField(
        queryset=Material.objects.filter(type_print=3),
        label="Выберите материал для печати",
        initial=1,  # по умолчанию ПВХ 3 мм
    )

    class Meta:
        model = Product
        fields = ["quantity", "material", "FinishWork", "images", "comments"]


class UploadFilesRollUp(forms.ModelForm):
    """Форма загрузки файлов для интерьерной печати полотна для Роллапа"""

    material = forms.ModelChoiceField(
        queryset=Material.objects.filter(id=2),
        label="Выберите материал для печати",
        initial=2,  # по умолчанию литой 450 грамм
    )
    FinishWork = forms.ModelChoiceField(
        queryset=FinishWork.objects.filter(id=2),
        label="Финишная обработка",
        initial=2,
    )

    class Meta:
        model = Product
        fields = ["quantity", "images"]
