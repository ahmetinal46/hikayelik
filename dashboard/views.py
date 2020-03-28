from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from articles.forms import ArticleForm
from django.contrib import messages
from articles.models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@login_required(login_url = "accounts:loginUser")
def myArticles(request):
    articles = Article.objects.filter(author = request.user)

    context={
        "articles":articles
    }
    return render(request,"includes/dashboard/content.html",context)


@login_required(login_url = "accounts:loginUser")
def dashboard(request):
    
    return render(request,"includes/dashboard/content.html")


def published(request):
    if request.user.is_superuser :
        page = request.GET.get('page', 1)
        articles = Article.objects.filter(published=False)
        paginator = Paginator(articles, 10)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        return render(request,"includes/dashboard/content.html",{"articles":articles})
    return redirect('index')


    
@csrf_protect
@login_required(login_url = "accounts:loginUser")
def PublishDone(request,id):
    if request.method == "GET":
        messages.info(request,"Bu işlemi doğru sıralamayı takip edin! (CSRF)")
        return  redirect("index")
    else:
        article = get_object_or_404(Article,id = id)
        if not request.user.is_superuser :
            messages.info(request,"Bu işlemi yapmak için yetkiniz yok")
            return  redirect("index")
        article.published=True
        article.save()
        messages.success(request,"Makale başarıyla yayınlandı.")
        return redirect("dashboard:published")

@login_required(login_url = "accounts:loginUser")
def PublishWaitingUser(request):
    articles = Article.objects.filter(author=request.user, published=False).order_by('created_date').reverse()
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request,"includes/dashboard/content.html",{"articles":articles})



    


