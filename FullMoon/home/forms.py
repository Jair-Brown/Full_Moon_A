from django import forms
from models import Herbs

class NameForm(forms.Form):
    herb = Herbs.objects.get(name = name)