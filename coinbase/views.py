# Create your views here.
from django.views.generic.base import TemplateView
from datetime import datetime
from django.http import HttpResponse
from .models import CoinbaseWallet


def balance(request):
    return HttpResponse("Balance $%s." % CoinbaseWallet.get_total_USD())


def orders(request):
    return HttpResponse("Orders %s." % CoinbaseWallet.orders())


def sell(request):
    return HttpResponse("Sell %s." % CoinbaseWallet.sell(100))


class CrowdfundingBoxStat(TemplateView):
    template_name = "statbox.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['start_date'] = datetime(2013, 12, 21)
        context['backers_count'] = CoinbaseWallet.get_orders_count()
        current_donations = CoinbaseWallet.get_total_USD()
        total_sum = 300000
        done = current_donations * 100 / total_sum
        context['current_balance'] = current_donations
        context['total_sum'] = total_sum
        context['done_percent'] = done
        context['rest_percent'] = 100 - done
        return context

class CrowdfundingOrderList(TemplateView):
    template_name = "orderlist.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['orders'] = CoinbaseWallet.orders()
        return context
