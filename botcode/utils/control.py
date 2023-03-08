# API for controlling the orders


from argparse import ArgumentParser
from ast import parse


import os
import sys
import json
import ccxt
from ccxt.base import errors
from pprint import pprint

from utils.options import red


class BinanceBot():
    def __init__(self):
        self.parser = ArgumentParser()

        self.workdir = os.path.join(os.path.expanduser("~"), '.mbot')
        self.data_file = os.path.join(self.workdir, 'data.json')
        self.symbol = ''
        self.limit = 0.0
        self.stop_loss_percent = 0.0
        self.target_percentage = 0.0
        self.stop_loss_cost = 0.0
        self.target_price_cost = 0.0
        self.process_inputs()

    def read_input(self):
        parser = self.parser

        parser.add_argument("-f", "--file",
                            default="",
                            type=str,
                            help="the csv file containing client data")

        parser.add_argument("-n", "--new-customer",
                            dest='new_customer',
                            default="",
                            type=str, nargs=6,
                            help="cutomer details as <name no space> <email> <api key> <secret key> <leverage> <lot")

        parser.add_argument("-d", "--del-customer",
                            dest='del_customer',
                            default="",
                            type=str,
                            help="api of the customer to delete")

        parser.add_argument("--sym",
                            dest='symbol',
                            default="",
                            type=str,
                            help="the symbol name")

        parser.add_argument("--limit",
                            dest='limit',
                            default=-1.0,
                            type=float,
                            help="limit price")

        parser.add_argument("--slc",
                            dest='stop_loss_cost',
                            default=-1.0,
                            type=float,
                            help="stop loss cost")

        parser.add_argument("--tpc",
                            dest='target_price_cost',
                            default=-1.0,
                            type=float,
                            help="target price cost")

        parser.add_argument("--sl",
                            dest='stop_loss_percent',
                            default=-1.0,
                            type=float,
                            help="stop loss percent")

        parser.add_argument("--tp",
                            dest='target_price_percent',
                            default=-1.0,
                            type=float,
                            help="target price percent")

        parser.add_argument("--reset",
                            dest='reset',
                            action='store_true',
                            help="Reset the json dump to a clean file")

        parser.add_argument("--co",
                            dest='cancel_orders',
                            action='store_true',
                            help="Cancel all orders in place")

        parser.add_argument("--run",
                            dest='run',
                            action='store_true',
                            help="run to see options and select")

        self.args = parser.parse_args()

    def consume_inputs(self):
        self.input_file = self.args.file
        self.reset = self.args.reset
        self.run = self.args.run
        self.symbol = self.args.symbol
        self.limit = self.args.limit
        self.stop_loss_percent = self.args.stop_loss_percent
        self.target_percentage = self.args.target_price_percent
        self.target_price = self.args.target_price_cost
        self.stop_loss_cost = self.args.stop_loss_cost

        self.cancel = self.args.cancel_orders
        self.new_customer = self.args.new_customer
        self.delete_customer = self.args.del_customer

    def create_json_dump(self):
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)

        if not os.path.exists(self.data_file) or self.reset :
            file = open(self.data_file, 'w')
            file.write('{}')
            file.close()
            print("Database reset")
            sys.exit()

    def read_data_file(self):
        with open(self.data_file, 'r') as fp:
            self.json_data = json.load(fp)

    def save_data_file(self):
        with open(self.data_file, 'w') as fp:
            json.dump(self.json_data, fp, indent=4)

    def print_current_api(self):
        for data in self.json_data.keys():
            print(data)

    def read_from_csv(self):
        from .reader import read_csv
        read_csv(self.json_data, self.input_file)

    def save_last_keys(self):
        name = input('Enter name ')
        mail = input('Enter email address')
        api_key = input('Enter a valid api key ')
        secret_key = input('Enter a valid secret key ')
        leverage = input('Enter leverage ')
        lots = input('Enter lot size ')

        if api_key not in self.json_data.keys():
            self.json_data[api_key] = {}

        self.json_data[api_key]['name'] = name
        self.json_data[api_key]['mail'] = mail
        self.json_data[api_key]['secret_key'] = secret_key
        self.json_data[api_key]['leverage'] = int(leverage)
        self.json_data[api_key]['lot'] = int(lots)
        self.save_data_file()

    def process_inputs(self):
        from .reader import validate_file

        self.read_input()
        self.consume_inputs()

        self.create_json_dump()
        self.read_data_file()


        if validate_file(self.input_file):
            self.read_from_csv()
            self.save_data_file()
            print("Clients added to database")
            return 0

        select = -1
        if self.run:
            from .options import create_options
            select = create_options()


        if select == 1:
            self.input_file = input("enter csv file name ")
            self.read_from_csv()
        elif select == 2:
            self.print_current_api()
        elif select == 3:
            self.save_last_keys()
        elif select == 4:
            self.symbol = input("enter symbol name ")
            limit = input("enter limit price")
            if len(self.limit) == 0:
                self.limit = -1
            else:
                self.limit = int(limit)
            self.place_order()
        elif select == 5:
            self.symbol = input("enter symbol ")
            self.cancel_order()
        elif select == 6:
            self.delete_customer = input("enter api to remove ")


        if len(self.delete_customer) > 0:
            if self.delete_customer in self.json_data.keys():
                self.json_data.pop(self.delete_customer)
                self.save_data_file()
            else:
                print('customer with api_key %s not found'%self.delete_customer)
            return 0

        if self.place_order():
            if self.limit < 1e-14:
                print('order - %s'%self.symbol)
            else:
                print('order - %f for %s'%(self.limit, self.symbol))
            return 0

        if self.cancel:
            if self.cancel_order():
                print("all current order cancelled")
                return 0

            if self.cancel_all_positions():
                print("all current position sold")
                return 0

    def load_api(self, api, secret, symbol):
        binance = ccxt.binanceus({
            "apiKey":api,
            "secret":secret,
            "options": {"defaultType": "spot", 'adjustForTimeDifference' : True},
            "timeout": 60000,
            "enableRateLimit": True,
        })

        # binance.verbose = True  # enable verbose mode after loading the markets
        print('-------------------------------------------------------------------')
        try:
            balance = binance.fetch_balance()
            pprint(balance['info']['accountType'])
            print(symbol.upper())
        except Exception as e:
            print('Failed to fetch the balance')
            print(type(e).__name__, str(e))
        order = None
        print('-------------------------------------------------------------------')
        _symbol = symbol.upper().removesuffix('USDT') + '/USDT'
        market = binance.market(_symbol)
        base = market['base']
        quote = market['quote']
        pprint(balance[base])
        pprint(balance[quote])

        return binance


    def place_order(self):
        if len(self.json_data.keys()) < 1:
            print("Client details missing")
            return False

        if len(self.symbol) == 0:
            return False

        if self.limit < 1e-14:
            self.order_type = 'MARKET'

        ordertype = 'MARKET'
        if self.limit > 0.0:
            ordertype = 'LIMIT'

        self.json_data['symbol'] = self.symbol

        for key in self.json_data.keys():
            if key == 'symbol':
                continue
            api_key = key
            secret = self.json_data[key]['secret_key']
            email = self.json_data[key]['email']
            leverage = int(self.json_data[key]['leverage'])
            lot_size = float(self.json_data[key]['lot'])

            binance = self.load_api(api_key, secret, self.symbol)
            price = binance.fetchOHLCV('BTCUSDT')[-1][1]

            params = {
                # 'test':True
            }

            order_send_result = None

            try:
                if ordertype == 'LIMIT':
                    order_send_result = binance.create_order(self.symbol.upper(), ordertype, "BUY", lot_size/price, self.limit, params)
                    print(f'\nBinanceOrder: \nclient = {email} \nOPEN market order sending result = \n{order_send_result}')
                else:
                    order_send_result = binance.create_order(self.symbol.upper(), ordertype, "BUY", lot_size/price, self.limit, params)
                    print(f'\nBinanceOrder: \nclient = {email} \nOPEN market order sending result = \n{order_send_result}')

                self.json_data[key]['orderid'] = order_send_result['id']
                self.json_data[key]['qnty'] = lot_size/price
            except Exception as e:
                print('Failed to place order for api %s'%key)
                print(red("Error:"), red(type(e).__name__), str(e))

        self.save_data_file()

        return True

    def cancel_all_positions(self):
        if len(self.json_data.keys()) < 2:
            print("Either no active order or client details missing")
            return False

        if not self.cancel:
            return False

        if "symbol" in self.json_data.keys():
            self.symbol = self.json_data['symbol']
        else:
            print("No existing positions")
            return False

        for key in self.json_data.keys():
            if key == 'symbol':
                continue
            api_key = key
            secret = self.json_data[key]['secret_key']
            leverage = int(self.json_data[key]['leverage'])
            lot_size = float(self.json_data[key]['lot'])
            email = self.json_data[key]['email']
            binance = self.load_api(api_key, secret, self.symbol)

            params = {
                # 'test':True
            }

            try:
                last_trades = binance.fetch_closed_orders(self.symbol.upper())
                side = last_trades[-1]['side']
                qty = float(self.json_data[key]['qnty'])
                if side == 'buy':
                    order_send_result = binance.create_order(self.symbol.upper(), "MARKET", "SELL", qty, None , params)
                    print(f'\nBinanceOrder: \nclient = {email} \nOPEN market order sending result = \n{order_send_result}')
                else:
                    print("Last order was sell order So cannot place sell order again for %s"%api_key)
            except Exception as e:
                print('Failed to sell position for api %s'%key)
                print(red("Error:"), red(type(e).__name__), str(e))

        self.save_data_file()

        return True

    def cancel_order(self):
        if len(self.json_data.keys()) < 2:
            print("Either no active order or client details missing")
            return False

        if not self.cancel:
            return False

        if "symbol" in self.json_data.keys():
            self.symbol = self.json_data['symbol']
        else:
            print("No existing positions")
            return False

        for key in self.json_data.keys():
            if key == 'symbol':
                continue
            api_key = key
            secret = self.json_data[key]['secret_key']
            email = self.json_data[key]['email']
            binance = self.load_api(api_key, secret, self.symbol)

            params = {
                # 'test':True
            }

            try:
                orderid = self.json_data[key]['orderid']
                print("orderid : ", orderid)
                if orderid is not None:
                    response = binance.cancel_order(orderid, self.symbol.upper())
                    print(f'\nBinanceOrder: \nclient = {email} \nOPEN market order sending result = \n{response}')
                self.json_data[key]['orderid'] = None
            except Exception as e:
                print('Failed to sell position for api %s'%key)
                print(red("Error:"), red(type(e).__name__), str(e))

        self.save_data_file()





