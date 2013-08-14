# Create your views here.
from django.http import HttpResponse
from .models import CoinbaseWallet


def balance(request):
    return HttpResponse("Balance $%s." % CoinbaseWallet.get_total_USD())


def orders(request):
    return HttpResponse("Orders %s." % CoinbaseWallet.orders())


def sell(request):
    return HttpResponse("Sell %s." % CoinbaseWallet.sell(100))
