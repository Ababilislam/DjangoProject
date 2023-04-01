from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post


# Create your views here.

class PostlistView(ListView):
    model = Post
    template_name = 'blog/Home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Home.html', context)


def about(request):
    return render(request, 'blog/about.html')
