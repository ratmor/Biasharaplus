



from django.contrib import admin
from django.urls import path
from Biasharaplusapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login/',views.login_views,name='login'),
    path('register/',views.register_views,name='register'),
]
