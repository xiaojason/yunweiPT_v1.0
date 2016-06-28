from user_management import models
from django import forms

class AuthModelForm(forms.ModelForm):

    class Meta:
        model = models.userinfo
        fields = ('username','password')
        widgets = {
            'username':forms.TextInput(attrs={"name":'username',"id":'exampleusername',"class":'form-control',"placeholder":'input your username'}),
            'password':forms.TextInput(attrs={"type":"password","name":'passwd',"id":'exampleInputPassword1',"class":'form-control',"placeholder":'input your password'}),
        }
