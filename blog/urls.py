from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:blog_id>',views.detail,name="detail"),
    path('new/',views.new,name='new'),
    path('create',views.create, name='create'),
    path('',views.home,name='home'),
    path('newblog/',views.blogpost,name="newblog"),
    path('<int:blog_id>/destroy',views.destroy,name="destroy"),
]