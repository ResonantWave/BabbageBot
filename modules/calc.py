import urllib2
import urllib

def execute(data):
   a = data.split()
   if a[0].lower() == 'calc':
      if len(a) > 1:
         try:
	    response = urllib2.urlopen('http://api.mathjs.org/v1/?expr=' + urllib.quote_plus(''.join(a[1:len(a)])))
            html = response.read()
            if response.getcode() == 200:
	       return 'Result: ' + str(html)
	 except Exception as e:
	    return 'Error: ' + str(e)
      else:
         return 'Syntax error: calc operation'
