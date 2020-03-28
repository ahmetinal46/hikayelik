from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,HttpResponseRedirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView





class ArticleDetailView(DetailView):
    model = Article
    template_name = 'includes/article/article.html'
    slug_field = 'hikaye_slug'
    
    
    

class ArticleCreateView(CreateView):
    model = Article
    fields = ['story_writer','email','title','content','article_image',"grade",'hikaye']
    template_name = "includes/article/addarticle.html"
    def form_valid(self, form):
        article = form.save(commit=False)
        article.save()
        messages.add_message(self.request, messages.INFO, 'Makaleniz onaylanınca yayınlanacaktır.')
        return redirect("articles:showArticles")


class ArticleListView(ListView):
    queryset = Article.objects.filter(published=True).order_by('created_date').reverse()
    context_object_name = 'articles'
    template_name = 'includes/article/article-list.html'
    paginate_by = 15

    


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ['story_writer','email','title','content','article_image',"grade",'hikaye']
    template_name = "includes/article/update.html"
    login_url = "loginUser"
    slug_field = 'hikaye_slug'
    def get_success_url(self):
        return reverse_lazy('articles:detail', kwargs={'slug': self.object.hikaye_slug})
    

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.save()
        messages.add_message(self.request, messages.INFO, 'Makaleniz düzenlendi.')
        return HttpResponseRedirect(self.get_success_url())
    
   
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if not request.user.is_authenticated:
            messages.add_message(self.request, messages.INFO, 'Bu düzenleme için giriş yapmalısınız.')
            return redirect("accounts:loginUser")
        if not request.user.is_superuser :
            messages.add_message(self.request, messages.INFO, 'Bu düzenleme için yetkiniz yoktu.')
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)

    

        
        


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    slug_field = 'hikaye_slug'
    success_url = reverse_lazy('articles:showArticles')
    template_name = "includes/article/article.html"


   
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if not request.user.is_superuser:
            messages.add_message(self.request, messages.INFO, 'Bu düzenleme için yetkiniz yoktu.')
            return redirect("index")
        messages.add_message(self.request, messages.WARNING, 'Makale başarıyla silindi.')
        return super().dispatch(request, *args, **kwargs)

    

class Grade1ListView(ListView):
    queryset = Article.objects.filter(published=True,grade=1).order_by('created_date').reverse()
    context_object_name = 'articles'
    template_name = 'includes/article/article-list.html'
    paginate_by = 15


class Grade2ListView(ListView):
    queryset = Article.objects.filter(published=True,grade=2).order_by('created_date').reverse()
    context_object_name = 'articles'
    template_name = 'includes/article/article-list.html'
    paginate_by = 15

class Grade3ListView(ListView):
    queryset = Article.objects.filter(published=True,grade=3).order_by('created_date').reverse()
    context_object_name = 'articles'
    template_name = 'includes/article/article-list.html'
    paginate_by = 15

class Grade4ListView(ListView):
    queryset = Article.objects.filter(published=True,grade=4).order_by('created_date').reverse()
    context_object_name = 'articles'
    template_name = 'includes/article/article-list.html'
    paginate_by = 15