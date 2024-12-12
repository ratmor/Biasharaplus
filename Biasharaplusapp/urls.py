



from django.contrib import admin
from django.urls import path
from Biasharaplusapp import views

urlpatterns = [
   
    path('home/',views.home),
    path('login/',views.login_views,name='login'),
    path('register/',views.register_views,name='register'),
    path('',views.index,name='index'),
    path('layout/',views.layout,name='layout'), # type: ignore
    path('service-details/',views.service_details,name='service-details'), # type: ignore
    path('portfolio-details/',views.portfolio_details,name='portfolio-details'), # type: ignore
    path('blog/',views.blog,name='blog'),
    path('blog-details/',views.blog_details,name='blog-details'),# type: ignore
    path('upload_image/',views.upload_image,name='upload_image'),
    path('payment/',views.Payment,name='payment'),
    path('stk/',views.stk,name='stk'),
    path('sendcontact/',views.contact,name='sendcontact'),
    path('contact/',views.insertcontact,name='contact'),
]
