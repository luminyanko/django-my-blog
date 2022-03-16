from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def showblog(request):
    posts = Post.objects.all
    return render(request, 'blog/blog.html', {'posts': posts})


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_view.html', {'post': post})