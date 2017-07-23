from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(label='Entity name', max_length=100)
    email = forms.EmailField(label='Entity email', max_length=100)
