from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect



# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"includes/about/about.html")

def detail(request,id):
    #article = Article.objects.filter(id = id).first
    article = get_object_or_404(Article,id = id)
    User = get_user_model()
    userinfo = get_object_or_404(User,id = article.author_id)
    return render(request,"includes/article/article.html",{"article":article,"user":userinfo})

@csrf_protect
@login_required(login_url = "accounts:loginUser")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturudu.")
        return redirect("articles:showArticles")
    return render(request,"includes/article/addarticle.html",{"form":form})

@csrf_protect   
@login_required(login_url = "accounts:loginUser")
def updateArticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    if not request.user.is_superuser and  article.author != request.user :
        messages.info(request,"Bu işlemi yapmak için yetkiniz yok")
        return  redirect("index")
    if form.is_valid():
        article = form.save(commit=False)
        article.save()
        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("/articles/article"+'/'+str(id))

    return render(request,"includes/article/update.html",{"form":form})

@csrf_protect
@login_required(login_url = "accounts:loginUser")
def deleteArticle(request,id):
    if request.method == 'POST':
        article = get_object_or_404(Article,id = id)
        if not request.user.is_superuser and  article.author != request.user :
            messages.info(request,"Bu işlemi yapmak için yetkiniz yok")
            return  redirect("index")
        article.delete()
        messages.success(request,"Makale başarıyla silindi.")
        return redirect("dashboard:dashboard")
    else:
        messages.info(request,"Bu işlemi doğru sıralamayı takip edin! (CSRF)")
        return  redirect("index")



def showArticles(request):
    keyword = request.GET.get("keywards")
    page = request.GET.get('page', 1)
    
    if keyword:
        articles = Article.objects.filter(title__contains=keyword).order_by('created_date').reverse()
        paginator = Paginator(articles, 10)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
         articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        
        return render(request,"includes/article/article-list.html",{"articles":articles})

    articles = Article.objects.filter(published=True).order_by('created_date').reverse()
    paginator = Paginator(articles, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,"includes/article/article-list.html",{"articles":articles})




