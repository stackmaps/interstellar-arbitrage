#Hardcode v

#download imports
import jason
import urllib2

#exhange api call
response = urllib2.urlopen('https://api.bitfinex.com/v1')
html = response.read()
#looking at ticker
bitfinex_ltc_btc_ticker = json.loads(html)
#looks at  particular ticker
bitfinex_ltc_btc_string = (bitfinex_ltc_btc_ticker)
print ("bitfinex")
print (bitfinex_ltc_btc_string)
#convert from string to float
bitfinex_ltc_btc_comparison = float(bitfinex_ltc_btc_string)

#Level 1 CREATE API FOR ANOTHER EXCHANGE (https://www.bitstamp.net/api/ticker/) AND COMPARE THE PRICES FINDING THE DIFFERENCE BETWEEN THEM ((V1-V2)/(V2+V2)/2)*100
#Level 2 LOOK AT DEAPTH OF ORDER TO AVOID SLIPAGE (TRY MULTIPLYING DEAPTH BY PRICE DIFFERENCE)
#Level 3 COMPARE ALL BIDS TO ASKS BETWEEN EXCHANGES
