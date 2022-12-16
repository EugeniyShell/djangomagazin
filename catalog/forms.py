from django import forms

from .models import ProductCategory, Product


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
