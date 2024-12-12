from .credentials import MpesaAccessToken, LipanaMpesaPpassword
import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from django.shortcuts import render, redirect
from .credentials import MpesaAccessToken, LipanaMpesaPpassword
from .models import Contact
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

def Payment(request):
    return render(request,'payment.html')

def token(request):
    consumer_key = '32SSlU9QYIbEOnnEqbX8choULrHmKVxOT0ARxr4UmBC1zAXB'
    consumer_secret = '6vLMggwlKVhExNi3vfEWXKdEINSjHL64MEmza0J3FrAxn78PBN8GOkeRqAp1XRQE'
    api_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'payment.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Glory",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment made successfull!")

def insertcontact(request):
    return render(request,'contact.html')
def contact(request):
    if request.method == 'POST':
            name = request.POST['name'],
            email = request.POST['email'],
            subject =request.POST['subject'],
            message = request.POST['message'],

            contact=Contact(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            contact.save()

    return redirect('/')
    
    return render (request,'contact.html')