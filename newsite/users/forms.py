from django import forms
from django.forms import ModelForm
from .models import User


class CreateUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    bio = forms.CharField()
    age = forms.IntegerField()
    sex = forms.CharField()
    create = forms.DateTimeField()


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'bio', 'age', 'sex', 'create'
        ]