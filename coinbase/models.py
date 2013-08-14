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
    def get_json_data(request, **kwargs):
        opener = build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        install_opener(opener)
        url = 'https://coinbase.com/api/v1/{0}?api_key={1}'
        url = url.format(request, CoinbaseWallet.secret_key())
        for k in kwargs:
            url += '&{0}={1}'.format(k, kwargs[k])
        data = urlopen(url).read().decode('utf-8')
        return json.loads(data)

    @staticmethod
    def balance():
        return CoinbaseWallet.get_json_data('account/balance')

    @staticmethod
    def orders():
        return CoinbaseWallet.get_json_data('orders')

    @staticmethod
    def sell(count):
        return CoinbaseWallet.get_json_data('prices/sell', qty=count)

    @staticmethod
    def get_total_USD():
        balance = CoinbaseWallet.balance()
        raise Exception(balance)
        total = 0.0
        for x in balance:
            if x['currency'] == 'BTC':
                x = CoinbaseWallet.sell(x['amount'])['total']
            if x['currency'] == 'USD':
                total += float(x['amount'])
        return total
