from django import forms
from django.forms import ModelForm

from locator.models import Patroller


class VolunteerForm(ModelForm):
    class Meta:
        model = Patroller
        fields = ['first_name', 'last_name', 'code_name', 'cell', 'armed', 'email', 'telegram', 'preferred_shifts', 'preferred_watchpoint']