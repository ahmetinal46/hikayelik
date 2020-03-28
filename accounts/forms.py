from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User as UserAuth
from django.forms import ValidationError
from .reserved_username_list import blacklist
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
 
#UserCreationForm miras alınıyor.ç
class MyUserCreationForm(UserCreationForm):
 
    class Meta:
        # Yeni Model
        model = User
        # Yeni alanlar
        fields = { 'username', 'password1', 'password2', 'email',}
        exclude = ['Avatar','gender','birth_date',]





    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if username in blacklist:
            raise  ValidationError("Lütfen başka bir kullanıcı adı seçin.")
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data.get("password1")    
        user.set_password(password)
        user.is_active= False
        user.save()
        current_site = Site.objects.get_current()
        mail_subject = 'Activate your blog account.'
        message = render_to_string('includes/emails/activation-mail.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.id)),
            'token':account_activation_token.make_token(user),
        })
        to_email = self.cleaned_data['email']
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        if commit:
            user.save()
        return user       


class MyAuthenticationForm(AuthenticationForm):
    
    def clean_username(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise  ValidationError("Kullanıcı adı veya şifre yanlış.")
        if user is not None and user.is_active== False:
            raise ValidationError("E-postanıza gelen bağlantıyı onaylarak hesabınızı aktif edin.")
        else:
            login(request, user)
        return username

class LoginForm(forms.Form):
    username=   forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget= forms.PasswordInput)




class UsernameAndEmailUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAuth
        fields = {'username','email'}

class AvatarGenderUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields = {'Avatar','gender','birth_date','location'}


class MyUserUpdateFormGeneral(UsernameAndEmailUpdateForm,AvatarGenderUpdateForm):
 
    class Meta:
        # Yeni Model
        model = User
        # Yeni alanlar
        fields = { 'username', 'email','Avatar','gender','birth_date','location'}
    def __init__(self, *args, **kwargs):
        super(MyUserUpdateFormGeneral, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs.update({'class': 'col-md-6'})
        #self.fields['email'].widget.attrs.update({'class': 'col-md-6'})
        #self.fields['Avatar'].widget.attrs.update({'class': 'inputFileVisible'})
        #self.fields['gender'].widget.attrs.update({'class': 'col-md-6'})
        #self.fields['birth_date'].widget.attrs.update({'class': 'col-md-6'})
        #self.fields['location'].widget.attrs.update({'class': 'col-md-6'})
    