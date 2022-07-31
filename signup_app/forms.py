from .models import User
from django import forms

class UserCreateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})