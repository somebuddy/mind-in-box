""" Coinbase API model

    Provides access to coinbase wallet.

    API version 1.0

    https://coinbase.com/api/doc

    API Key must be enabled, see:
        https://coinbase.com/account/integrations
"""
from os import environ
from aniso8601 import parse_datetime
from time import strftime
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
        orders = CoinbaseWallet.get_json_data('orders')['orders']
        orders_list = []
        for x in orders:
            x = x['order']
            coins = int(x['total_btc']['cents'])/100000000.0
            dt = parse_datetime(x['created_at']).utctimetuple()
            ds = strftime("%a, %d %b %Y", dt)
            ts = strftime("%H:%M:%S", dt)
            if x['status'] == 'completed':
                orders_list.append([x['id'], coins, ds, ts])
        return orders_list

    @staticmethod
    def get_orders_count():
        return len(CoinbaseWallet.orders()) 

    @staticmethod
    def sell(count):
        return CoinbaseWallet.get_json_data('prices/sell', qty=count)

    @staticmethod
    def get_total_USD():
        balance = CoinbaseWallet.balance()
        for k, x in balance.items():
            print(k)
        total = 0.0
        if balance['currency'] == 'BTC':
            balance = CoinbaseWallet.sell(balance['amount'])['total']
        if balance['currency'] == 'USD':
            total += float(balance['amount'])
        return max(0, total)
