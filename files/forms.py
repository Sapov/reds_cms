from django import forms

from files.models import Material, Product


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
