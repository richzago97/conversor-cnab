from django import forms


class UploadCnbalForm(forms.Form):
    file = forms.FileField()
