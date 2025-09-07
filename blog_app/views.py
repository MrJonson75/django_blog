import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
created_yars = os.environ.get('YARS_CREATED', datetime.datetime.now().year)

def index(request):
    data = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {
        'posts': data,
        'year': created_yars,
    }
    return render(request, 'blog_app/index.html', context)

def post_detail(request, slug):
    pass

def category_detail(request, slug):
    pass

def category_list(request):
    pass

def tag_detail(request, slug):
    pass

def about(request):
    pass


