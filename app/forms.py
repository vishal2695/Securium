from django import forms
from django.contrib.auth.models import User


class usersignupfrm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Username'})
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter your first name'})
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter your last name'})
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Email is not valid'})
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Password'})
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Re-Enter password'})

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname):
            raise forms.ValidationError('Username already taken.')
        return uname

    def clean_email(self):
        uemail = self.cleaned_data['email']
        if User.objects.filter(email=uemail):
            raise forms.ValidationError('Your email is already registered.')
        return uemail

    def clean_password2(self):
        upass = self.cleaned_data['password2']
        if len(upass)<8:
            raise forms.ValidationError('password must be more than 8 character.')
        return upass

class userloginfrm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Username'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Password'})

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname):
            return uname
        else:
            raise forms.ValidationError('Invalid Username')