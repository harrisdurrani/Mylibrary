from django import forms
from .models import LibraryCardModel
class LibraryCardForm(forms.ModelForm):
    class Meta:
        model = LibraryCardModel
        fields = ['user_email', 'first_name', 'last_name']
    #last_name = forms.CharField(widget=forms.Textarea, required=True)

