



from django.contrib import admin
from django.urls import path
from Biasharaplusapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/',views.index,name='index'),
    path('starter-page/',views.starter,name='starter-page'),
    path('service-details/',views.service,name='service-details'),
    path('blog/',views.blog,name='blog'),
    path('blog-details/',views.details,name='blog-details'),
]
