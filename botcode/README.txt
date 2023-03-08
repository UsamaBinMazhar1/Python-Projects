Option 1:

python binance_bot.py -h

This command will print all the options available


python binance_bot.py -f test.csv

here test.csv is the file containing all the api, secret and order details
in csv format. The code will read the data and execute the order in the
file.

python binance_bot.py --sym <sym_name> --limit 20

This command will place the order for all the api in the database

python binance_bot.py --co

This will cancel all the current order in place and all positions