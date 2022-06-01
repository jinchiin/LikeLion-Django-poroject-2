from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create(request):
    if request.method = 'POST':
        form = PostForm(request.POST, request.FILES)
    return redirext('index')
else:
    form = PostForm()
    return render(requests, 'create.html', {'form': form})

# Create your views here.
