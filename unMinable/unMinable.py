from binance.client import Client
import multiprocessing.dummy
import numpy as np
import requests
import json


pool = multiprocessing.dummy.Pool(4)

class unMinable:
    def __init__(self, MHs, algo):
        self.MHs = MHs
        self.algo = algo 
        self.reward_day = {}

        self.urls()

        self.client = Client()

    def urls(self):
        self.base_url = 'https://api.unminable.com/v3'
        self.url_coins = self.base_url + '/coins'
        self.url_calculator = self.base_url + '/calculate/reward'

    def manage_request(self, method, url, data={}):
        try:
            response = requests.request(method, 
                                        url, 
                                        data=data)
            response.status_code
            return response

        except requests.exceptions.HTTPError as errh:
            print ('Http Error:',errh)
            quit()

        except requests.exceptions.ConnectionError as errc:
            print ('Error Connecting:',errc)
            quit()

        except requests.exceptions.Timeout as errt:
            print ('Timeout Error:',errt)
            quit()

        except requests.exceptions.RequestException as err:
            print ('OOps: Something Else',err)
            quit()

    def get_symbol(self):
        response = self.manage_request('GET', self.url_coins)
        self.symbol = [r['symbol'] for r in response.json()['coins']]

    def menage_get_reward(self):
        self.get_symbol()
        pool.map(self.get_reward, self.symbol) 
        pool.close()
        pool.join()

    def get_reward(self, symbol):
        data = {'mh':self.MHs,
                'algo':self.algo,
                'coin':symbol}
        response = self.manage_request('POST', self.url_calculator, data)
        self.reward_day[symbol] = response.json()['per_day']

    def conversion(self):
        tikers = self.client.get_all_tickers()
        symbol_accepted = [t['symbol'].split('USDT')[0] for t in tikers if t['symbol'].split('USDT')[0] in self.symbol]
        self.reward_day_usdt = {symbol + 'USDT': [np.round(float(t['price']) *\
                                                           self.reward_day[symbol], 4)
                                                  for t in tikers if t['symbol']==symbol + 'USDT'][0] 
                                for symbol in symbol_accepted}
        self.reward_day_usdt = dict(sorted(self.reward_day_usdt.items(), key=lambda k: k[1], reverse=True))


if __name__ == '__main__':
    MHs = 25, 
    algo = 'ethash'

    un_minable = unMinable(MHs, algo)
    un_minable.menage_get_reward()
    un_minable.conversion()
    print(json.dumps(un_minable.reward_day_usdt, indent=1))

