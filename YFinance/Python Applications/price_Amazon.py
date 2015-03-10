import time
from yahoo_finance import Share
price = Share('AMZN')
print price.get_info()
print price.get_open()
print price.get_price() + " at " + price.get_trade_datetime()
for x in range(0, 28):
	time.sleep(60)
	from yahoo_finance import Share
	price = Share('AMZN')
	print price.get_price() + " at " + price.get_trade_datetime()
print "Data pulling completed."
