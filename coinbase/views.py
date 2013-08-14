# Create your views here.
from django.http import HttpResponse
from .models import CoinbaseWallet


def balance(request):
    return HttpResponse("Balance %s." % CoinbaseWallet.balance())


def orders(request):
    return HttpResponse("Orders %s." % CoinbaseWallet.orders())


def sell(request):
    return HttpResponse("Sell %s." % CoinbaseWallet.sell())
