from django.shortcuts import render,redirect,get_object_or_404
from .forms import MyUserCreationForm,LoginForm,MyUserUpdateFormGeneral
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login, authenticate,logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.conf import settings
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
# Create your views here.

def register(request):
    form = MyUserCreationForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        email = form.cleaned_data.get("email")

        newUser = User(username = username,email=email, is_active = False,)
        newUser.set_password(password)      
        #newUser.save()        
        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('includes/emails/activation-mail.html', {
            'user': newUser,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(newUser.pk)).decode('utf-8'),
            'token': account_activation_token.make_token(newUser),
            })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        newUser.save()
        messages.success(request,"Hesabınızı aktif etmek için lütfen E-posta adresinize gelen maildeki linke tıklayınız!")

        return redirect("index")

    contex = {
        "form": form
    }
    
    return render(request,"includes/user/register.html",contex)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password =  form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)
        if user is not None and user.is_active == False:
            messages.info(request,"Kullanıcı kaydı onaylanmamış lütfen e-posta adresinizi kontrol ediniz.<br><a href=\"http://www.google.com\">Onay E-postasını tekrar yolla!</a>")
            return redirect("index") 
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı.")
            return render(request,"includes/user/login.html",context)
        
        
        
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        dj_login(request,user)
        return redirect("index")
  
    return render(request,"includes/user/login.html",context)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        # activate user and login:
        user.is_active = True
        user.save()
        dj_login(request,user)
        messages.success(request, 'Hesabınız başarıyla aktifleştirildi.')
        return redirect("index")
    else:
        return HttpResponse('Aktivasyon başarısız veya hesap zaten aktif!')
            
def profileView(request,username):
    User = get_user_model()
    user = get_object_or_404(User,username = username)
    context = {
        "user":user
    }
    return render(request,"includes/profile/profile.html",context)     




@login_required(login_url = "user:loginUser")
def userSettings(request,username):
    User = get_user_model()
    user = get_object_or_404(User,username = username)
    form = MyUserUpdateFormGeneral(request.POST or None, request.FILES or None, instance=user)
    if not request.user.is_superuser and  user != request.user :
        messages.info(request,"Bu işlemi yapmak için yetkiniz yok")
        return  redirect("index")
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        messages.success(request,"Profil başarıyla güncellendi.")
        return redirect("user:settings",username)
        
    return render(request,"includes/user/settings/content.html",{"form":form})