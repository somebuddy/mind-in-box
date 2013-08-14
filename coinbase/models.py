""" Coinbase API model

    Provides access to coinbase wallet.

    API version 1.0

    https://coinbase.com/api/doc

    API Key must be enabled, see:
        https://coinbase.com/account/integrations
"""
from os import environ
from urllib.request import urlopen, build_opener, install_opener
import json


class CoinbaseWallet(object):
    @staticmethod
    def secret_key():
        return environ['COINBASE_API_KEY']

    @staticmethod
    def get_json_data(request):
        opener = build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        install_opener(opener)
        url = 'https://coinbase.com/api/v1/{0}?api_key={1}'
        url = url.format(request, CoinbaseWallet.secret_key())
        data = urlopen(url).read().decode('utf-8')
        return json.loads(data)

    @staticmethod
    def balance():
        return str(CoinbaseWallet.get_json_data('account/balance'))

    @staticmethod
    def orders():
        return str(CoinbaseWallet.get_json_data('orders'))

    @staticmethod
    def sell():
        return str(CoinbaseWallet.get_json_data('prices/sell'))
