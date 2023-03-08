# API for reading different scenarios
import json
import os
import sys

import numpy as np
import csv

def validate_file(filename):
    if len(filename) < 1:
        return False
    if not os.path.exists(filename):
        print(filename , " file does not exists, please check")
        return False
    return True


def read_csv(json_df, csvfile):
    fp = open(csvfile, 'r')

    csvreader = csv.reader(fp)
    # skip header
    next(csvreader)

    try:
        for row in csvreader:
            key = row[2]
            if not key in json_df.keys():
                json_df[key] = {}
            json_df[key]['name'] = row[0]
            json_df[key]['email'] = row[1]
            json_df[key]['secret_key'] = row[3]
            json_df[key]['leverage'] = row[4]
            json_df[key]['lot'] = row[5]

    except:
        print('Cannot read file ', csvfile)
        msg = '''
        Required format is

        name, email, api, secret, leverage, lot
        John Doe, email@email, Fov0aFs.., YyHGgzA.., 1, 21
        ...
        see test.csv
        '''
        print(msg)
        sys.exit()



def read_order_file(json_df, filename):

    try:
        leverages, lots = np.loadtxt(filename,
                                     delimiter=',',
                                     skiprows=1,
                                     unpack=True)
    except:
        print('Cannot read file ', filename)
        msg = '''
        Required format is

        leverage, lots
        1, 21
        3, 45
        ...
        see order.csv
        '''
        print(msg)
        sys.exit()

    print(leverages, lots)

    api = json_df['last']['api']
    sec = json_df['last']['secret']

    print("Last api and secret keys are")
    print("api ", api)
    print("secret ", sec)

    yes = ''
    while not ((yes == 'y') or (yes == 'n')):
        yes = input('Is the api correct (y/n) ')

    if yes:
        if not api in json_df.keys():
            json_df[api] = {}
        json_df[api]['secret_key'] = sec
        arr = None
        if 'orders' in json_df[api].keys():
            arr = json_df[api]['orders']
        else:
            json_df[api]['orders'] = []
            arr = json_df[api]['orders']
        for i, lot in enumerate(lots):
            arr.append({'leverage': int(leverages[i]), 'lot': int(lots[i])})
