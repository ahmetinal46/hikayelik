from django.contrib import admin
from django.urls import path
from .views2 import ArticleDetailView,ArticleCreateView,ArticleListView,ArticleUpdateView,ArticleDeleteView,Grade1ListView,Grade2ListView,Grade3ListView,Grade4ListView

app_name = "articles"

urlpatterns = [
    path('hikaye-gonder/',ArticleCreateView.as_view(),name="addarticle"),
    path('hikaye/<slug:slug>/',ArticleDetailView.as_view(),name="detail"),
    path('update/<slug:slug>/',ArticleUpdateView.as_view(),name="update_article"),
    path('delete/<slug:slug>/',ArticleDeleteView.as_view(),name="delete_article"),
    path('',ArticleListView.as_view(),name="showArticles"),
    path('sınıf-1/',Grade1ListView.as_view(),name="showGrade1"),
    path('sınıf-2/',Grade2ListView.as_view(),name="showGrade2"),
    path('sınıf-3/',Grade3ListView.as_view(),name="showGrade3"),
    path('sınıf-4/',Grade4ListView.as_view(),name="showGrade4"),
   
    
]