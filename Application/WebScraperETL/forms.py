from django import forms
from .models import Opinion
from .models import ProductID

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductID
        fields = ["productID"]

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ["username", "productRating", "productReview"]