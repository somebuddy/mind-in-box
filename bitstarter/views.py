from django.views.generic.base import TemplateView
from datetime import datetime
from coinbase.models import CoinbaseWallet

class BitstarterView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['start_date'] = datetime(2013, 12, 15)
        context['backers_count'] = 0#CoinbaseWallet.get_orders_count()
        context['current_balance'] = 0#CoinbaseWallet.get_total_USD()
        context['orders'] = []#CoinbaseWallet.orders()
        return context
