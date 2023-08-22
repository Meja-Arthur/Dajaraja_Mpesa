from django.shortcuts import render
from django.http import HttpResponse
#mpesa import 
from django_daraja.mpesa.core import MpesaClient
# Create your views here.


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0745866717'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'MPESA TEST'
    callback_url = 'https://85f0-102-215-76-65.ngrok.io';# this callback_url must be a live url
    response = cl.stk_push(phone_number, 
            amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body
        return HttpResponse("STK Push in Django👋")
    
    # you should get a response like this when you use the above codes 
# { "MerchantRequestID":"23520-158347504-2", "CheckoutRequestID":"ws_CO_22082023113829699745866717", "ResponseCode": "0", 
#  "ResponseDescription":"Success. Request accepted for processing", "CustomerMessage":"Success. Request accepted for processing" }    