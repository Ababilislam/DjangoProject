from django.shortcuts import render

# Create your views here.
def home(self,request):
    return render(request, 'blog/Home/html',name="home")
