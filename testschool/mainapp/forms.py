from django import forms


class FileForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    date = forms.DateField()
    afile = forms.FileField()