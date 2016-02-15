import urllib2
import json

def execute(data):
   a = data.split()
   if a[0].lower() == 'chucknorris': 
      try:
         response = urllib2.urlopen('http://api.icndb.com/jokes/random')
         html = response.read()
         decoded = json.loads(html)

         return decoded['value']['joke']
      except Exception as e:
         return (str(e))
