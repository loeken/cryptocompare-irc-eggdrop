import requests
r0 = requests.get('https://min-api.cryptocompare.com/data/dayAvg?fsym=BTC&tsym=USD')
d0 = r0.json()
r1 = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD')
r2 = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
d1 = r1.json()
d2 = d1['RAW']
d3 = d2['BTC']
d4 = d3['USD']
d5 = r2.json()
X = str( d0['USD'] )		# AVERAGE OF THE DAY
P = str( d4['PRICE'] )		# PRICE CURRENTLY
O = str( d4['OPENDAY'] )	# OPENING PRICE
H = str( d4['HIGHDAY'] )	# HIGH OF THE DAY
L = str( d4['LOWDAY'] )		# LOW OF THE DAY
A = str( d5['USD'] )

ICON_UP   = 'H'
ICON_DOWN = 'L'


print('\0030BTC \00314-\0030 @\00314$' + P + ' - \0030' + ICON_UP + '\0033$' + H + ' \0030' + ICON_DOWN + '\0035$' + L + ' \00314- \0030X\00314$' + X + ' ' + '\0030A\00314$' + A)
