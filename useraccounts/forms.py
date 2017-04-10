from django import forms
from django.forms import CharField,Form,PasswordInput
from django.contrib.auth.models import User
from .models import UserProfle,Todos


class RegistrationForm(forms.Form):
    username = forms.CharField(label = 'Username',max_length=50,required=True)
    first_name = forms.CharField(label = 'First name',required=True,max_length=140)
    last_name = forms.CharField(label = 'Last name',max_length=140,required=False)
    email = forms.EmailField(label = 'Email', max_length=50,required=True)
    password = forms.CharField(label='Password',widget=PasswordInput(),required=True)
    address = forms.CharField(label='Address', max_length=250,required=False)


class LoginForm(forms.Form):
    email = forms.EmailField(label = 'Email', max_length=50,required=True)
    password = forms.CharField(label='Password',widget=PasswordInput(),required=True)


class EditForm(forms.ModelForm):
    username = forms.CharField(label = 'Username',max_length=50,required=True)
    first_name = forms.CharField(label = 'First name',required=True,max_length=140)
    last_name = forms.CharField(label = 'Last name',max_length=140,required=False)
    # password = forms.CharField(label='Password',widget=PasswordInput(),required=True)
    address = forms.CharField(label='Address', max_length=250,required=False)

    class Meta:
        model = User
        exclude = ('email','last_login','is_superuser','is_staff','is_active','date_joined','groups','user_permissions','password')

class PasswordResetForm(forms.Form):
    password = forms.CharField(label='Password',widget=forms.PasswordInput,required=True)
    password_confirm = forms.CharField(label='Confirm Password',widget=forms.PasswordInput,required=True)


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label = 'Email', max_length=50,required=True)


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todos
        exclude = ('user','status','created_at','updated_at','done_by')


class TodoEditForm(forms.ModelForm):
    status = forms.ChoiceField(choices=[('True','Done'),('False','In-progress')])
    class Meta:
        model = Todos
        exclude = ('user','created_at','updated_at')
