from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.

def home(request):
    blogs = Blog.objects #model로 부터 객체 목록을 받아오는 .objects 
    #쿼리셋 #메소드

    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request,'detail.html',{'blog':blog_detail})

#new.html을 띄워주는 함수
def new(request):
    return render(request,'new.html')

#입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
