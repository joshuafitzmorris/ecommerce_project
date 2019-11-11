from django.shortcuts import render

import stripe
stripe.api_key = "sk_test_SiPaE5LzttrsrT6fdxXwXbXa00ykr9dtCr"
STRIPE_PUB_KEY = 'pk_test_iWK0KiaMkmLLLhzxJldzqLpy00hRxvSgRi'

def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {"publish_key" : STRIPE_PUB_KEY})