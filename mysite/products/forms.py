from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nombre')
    description = forms.CharField(max_length=300, label='Descripción')
    price = forms.DecimalField(max_digits=5, decimal_places=2, label='Precio')
    avalible = forms.BooleanField(initial=True, label='Disponible', required=True)
    photo = forms.ImageField(label="photo",required=False)

    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            avalible = self.cleaned_data['avalible'],
            photo = self.cleaned_data['photo'],
        )