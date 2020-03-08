from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    req_str = f'{request.user}'
    return HttpResponse(f'<h2>Hello {req_str}, Login Successfull</h2>')

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
    
def postdetail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_detail.html', {'object': post})

def postupdate(request, id):
    pass

def postdelete(request, id):
    pass
    



