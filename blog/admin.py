from django.contrib import admin
from .models import Blog
# Register your models here.

admin.site.register(Blog) #models.py에 만든 Blog클래스를 admin 사이트에 등록한다 