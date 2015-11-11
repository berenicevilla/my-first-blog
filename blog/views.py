from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render_to_response('blog/post_list.html', context)


