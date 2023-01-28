from django import forms
from .models import TransactionModel


class UploadCnbalForm(forms.Form):
    file = forms.FileField()
