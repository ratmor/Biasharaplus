from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def blog(request):
    return render(request, 'blog.html')

def details(request):
    return render(request, 'blog-details.html')

def services(request):
    return render(request, 'featured services.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def spotlight(request):
    return render(request, 'spotlight.html')

def contact(request):
    return render(request, 'contact.html')
