import urllib2
import json

def execute(data):
   a = data.split()
   if a[0].lower() == 'btc': 
      if len(a) > 1:
         if a[1].upper() == 'USD' or a[1].upper() == 'EUR': 
            try:
	       response = urllib2.urlopen('https://api.bitcoinaverage.com/ticker/global/' + a[1].upper())
	       html = response.read()
	       decoded = json.loads(html)
	       string = 'Prices BTC: \n24h Average: ' + str(decoded['24h_avg']) + '\nLast: ' + str(decoded['last']) + '\n24h volume: ' + str(decoded['volume_btc'])
	       if len(a) > 2:
	          if a[2].replace('.','',1).isdigit():
	             string += '\n' + str(a[2]) + " " + str(a[1].upper()) + ' -> BTC: ' + str(float(a[2]) / decoded['ask'])
	          else:
	             string += '\nError: The specified quantity is not a number'
               return string
	    except Exception as e:
	       return str(e)
	 else:
	    return 'Error: ' + a[1].upper() + ' is not a valid currency.'
      else:
         return 'Syntax error: btc (USD|EUR) <quantity>'
