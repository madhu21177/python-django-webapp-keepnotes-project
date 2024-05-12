from django import forms
from .models import memo
 
 
class memoForm(forms.ModelForm):
    class Meta:
        model = memo
        fields = "__all__"
