import time
from yahoo_finance import Share
price = Share('GOOG')
print price.get_open()
print price.get_price() + " at " + price.get_trade_datetime()
#for x in range(0, 28):
#	time.sleep(60)
#	price = Share('COMPANY CODE')
#	print price.get_price() + " at " + price.get_trade_datetime()
#print "Data pulling completed."
