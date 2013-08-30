from django.views.generic.base import TemplateView
from datetime import datetime
from coinbase.models import CoinbaseWallet

class BitstarterView(TemplateView):
    template_name = "index.html"

