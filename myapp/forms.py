from django import forms
from .models import tododb

class todoform(forms.ModelForm):
    class Meta:
        model=tododb
        fields="__all__"
        name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter task name'}))