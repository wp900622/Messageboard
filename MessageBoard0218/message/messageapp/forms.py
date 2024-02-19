from django import forms
from captcha.fields import CaptchaField

class PostForm(forms.Form):
    boardsubject = forms.CharField(max_length=100,initial='')
    boardname = forms.CharField(max_length=20, initial='')
    
    boardEmail = forms.EmailField(max_length=100,required=False)
    boardcontent = forms.CharField()
    captcha = CaptchaField()
