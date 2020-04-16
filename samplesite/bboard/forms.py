from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import json
from django import forms
from django.contrib.auth.models import User



class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = (('username', 'password'))

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (('username', 'password'))
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class JsonFormnew(forms.Form):
    JsonDatoForread = forms.CharField( required=True, widget =forms.Textarea(attrs=

                                                                             {'placeholder': 'Description',
                                                                                 'rows': 15}))
    def clean_JsonDatoForread(self):
        Json_passed = self.cleaned_data.get('JsonDatoForread')

        try:
            p = json.loads(Json_passed)
        except:
            raise ValidationError('String is not a jsonstring')

        if type(p) is int:

            raise ValidationError('String is not a jsonstring. It is a number')

        return Json_passed




