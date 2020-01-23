from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    
    context={'app001_list': Post.objects.all()}
    return  render(request, 'app001/index.html', context=context)
