# options for the use

def create_options():
    opts = r'''
    1: read customer data
    2: print current customer data
    3: put details of new customer
    4: new order
    5: close all orders
    6: remove a customer
    '''

    optints = [1, 2, 3, 4, 5, 6]
    print(opts)
    selection = -1
    while not (selection in optints):
        selection = int(input('Select a valid option '))

    return selection

def style(s, style):
    return style + s + '\033[0m'


def green(s):
    return style(s, '\033[92m')


def blue(s):
    return style(s, '\033[94m')


def yellow(s):
    return style(s, '\033[93m')


def red(s):
    return style(s, '\033[91m')


def pink(s):
    return style(s, '\033[95m')
