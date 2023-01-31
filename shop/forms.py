from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ('customer','product','email')
        labels = {'customer':'Your name','product':'Choose product','email':'Your email'}