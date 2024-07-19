from django.contrib import admin

from .models import (
    Material,
    Product,
    TypePrint,
    FinishWork,
    StatusProduct,
    UseCalculator,
)

admin.site.register(FinishWork)
admin.site.register(TypePrint)


class MaterialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Material._meta.fields]
    list_editable = ["price_contractor", "price", "price_customer_retail", "is_active"]
    list_filter = ["type_print"]
    sortable_by = ["type_print"]

    class Meta:
        model = Material


admin.site.register(Material, MaterialAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class UseCalculatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UseCalculator._meta.fields]
    # list_editable = ["price_contractor", "price", "price_customer_retail", "is_active"]
    list_filter = ["created_at", 'material']
    sortable_by = ["created_at"]

    class Meta:
        model = UseCalculator


admin.site.register(UseCalculator, UseCalculatorAdmin)



class FinishWorkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FinishWork._meta.fields]
    list_editable = ["price_contractor", "price", "price_customer_retail", "is_active"]

    class Meta:
        model = FinishWork


admin.site.register(FinishWork, FinishWorkAdmin)


class TypePrintAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TypePrint._meta.fields]

    class Meta:
        model = TypePrint


admin.site.register(TypePrint, TypePrintAdmin)
admin.site.register(StatusProduct)
