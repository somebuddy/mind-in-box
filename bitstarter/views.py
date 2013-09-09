from django.views.generic.base import TemplateView
from datetime import datetime
from coinbase.models import CoinbaseWallet
from django.conf import settings

class BitstarterView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(BitstarterView, self).get_context_data(**kwargs)
        context['debug'] = settings.DEBUG
        return context
