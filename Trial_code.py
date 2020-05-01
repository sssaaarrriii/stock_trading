import robin_stocks;
from robin_stocks import *;
robin_stocks.login("sariabukhadra@gmail.com","sariadirowi");
my_stocks = robin_stocks.build_holdings();
for key,value in my_stocks.items():
    print(key,value)


optionData = robin_stocks.find_options_for_list_of_stocks_by_expiration_date(['ba','ccl'], expirationDate='2020-04-17',optionType='put')
for item in optionData:
    print(' price -',item['strike_price'],' exp - ',item['expiration_date'],' symbol - ',item['chain_symbol'],' delta - ',item['delta'],' theta - ',item['theta'])


robin_stocks.logout();
