from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    blogs = Blog.objects #model로 부터 객체 목록을 받아오는 .objects 
    #쿼리셋 #메소드
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세개를 한 페이지로 자르기
    paginator = Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs,'posts':posts})

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
