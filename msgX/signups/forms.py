from django import forms
from .models import Signup
class SignUpform(forms.ModelForm):
    class Meta:
        model=Signup