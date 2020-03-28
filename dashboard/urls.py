from django.contrib import admin
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('published/',views.published,name="published"),
    path('publishdone/<int:id>',views.PublishDone,name='publishdone'),
    path('publishwaitinguser/',views.PublishWaitingUser,name='publishwaitinguser'),
    path('my-articles/',views.myArticles,name='myArticles'),
     
    
   
    
]