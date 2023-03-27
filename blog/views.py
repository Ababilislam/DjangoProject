from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author':'ab',
        'title':'blog post1',
        'content':'first post of the content',
        'date_posted': 'august 28, 2023'
    },
{
        'author':'udoy',
        'title':'blog post2',
        'content':'second post of the content',
        'date_posted': 'august 30, 2023'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/Home.html', context)


def about(request):
    return render(request, 'blog/about.html')