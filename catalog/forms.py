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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-select'})
        if 'category' in self.errors:
            self.fields['category'].widget.attrs.update(
                {'class': 'form-select is-invalid'})
        # self.fields['category'].empty_label = None
        self.fields['category'].required = False
