from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=100)
    email = forms.EmailField(label='Email: ')
    age = forms.IntegerField(label='Age: ')