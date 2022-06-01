from django.shortcuts import render
from .models
import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
    
def create(request):
    form = PostForm()
    return render(request, 'create.html', {'form': form})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('index')

def update(request,id):
    post = get_object_or_404(Post, id = id)
    if request.method = 'POST':
        
    else:
        form = PostForm()
        return render(request, 'update.html', {'form': form})