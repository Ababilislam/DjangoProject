from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1> this is home page</h1>')
    # return render(request, 'blog/Home/html', name="home")

def about(request):
    return HttpResponse('<h2>this is about page</h2>')
