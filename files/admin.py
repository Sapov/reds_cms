from django.contrib import admin

from .models import (
    Material,
    Product,
    TypePrint,
    FinishWork,
    StatusProduct,
    UseCalculator,
)

admin.site.register(Material)
admin.site.register(FinishWork)
admin.site.register(Product)
admin.site.register(TypePrint)