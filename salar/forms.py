
from django import forms
from users.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'quantity', 'description', 'image', 'category']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Product Name',
            'price': 'Product Price',
            'quantity': 'Available Quantity',
            'description': 'Product Description',
            'image': 'Product Image',
            'category': 'Product Category',
        }
      
        error_messages = {
            'name': {
                'max_length': "The product name is too long.",
            },
            'price': {
                'invalid': "Enter a valid price.",
            },
            'quantity': {
                'invalid': "Enter a valid quantity.",
            },
        }
