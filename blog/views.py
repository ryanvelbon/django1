from django.shortcuts import get_object_or_404, render
from .models import Post


def post_index(request):
    posts = Post.objects.order_by('-created_at')[:12]
    return render(request, 'posts/index.html', {'posts': posts})

def post_show(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/show.html', {'post': post})
