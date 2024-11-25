from django import forms
from .models import Watches



class WatchForm(forms.ModelForm):
    class Meta:
        model = Watches
        fields = "__all__"