from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_views(request):
    return render(request,'login.html')

def register_views(request):
    return render(request, 'register.html')