from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import MyUserCreationForm,MyUserUpdateFormGeneral
from django.contrib.auth.views import LoginView
from .forms import LoginForm,MyAuthenticationForm
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm








class SignUpView(SuccessMessageMixin, CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('accounts:loginUser')
    template_name = 'includes/user/register.html'
    success_message = "E-posta adresinize gelen mesajdaki onay bağlantısına tıkalayrak üyeliğini tamamlayabilirsiniz."


        

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'includes/user/login.html'


    




class UserUpdateView(UpdateView):
    model = User
    form_class = MyUserUpdateFormGeneral
    template_name="includes/user/settings/content.html"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, username=self.request.user.username)

    def get_success_url(self):
        return reverse_lazy('accounts:profileView', kwargs={'username': self.object.username})
