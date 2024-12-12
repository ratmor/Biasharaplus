from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_views(request):
    return render(request,'login.html')

def register_views(request):
    return render(request, 'register.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def layout(request):
    return render(request, 'layout.html')

def upload_image(request):
    return render(request, 'upload_image.html')
