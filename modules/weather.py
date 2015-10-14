# -*- coding: utf-8 -*-
import urllib2
import logging
import json
import os

token = "" # YOUR OPENWEATHERMAP ID GOES HERE
token = os.environ['TOKENWEATHER'] # DELETE THIS

def execute(data):
   a = data.split()
   if a[0].lower() == 'weather':
      if len(a) > 1:
         try:
            response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + a[1].lower() + '&units=metric&appid=' + token) 
            html = response.read()
            decoded = json.loads(html)
            string = 'Temperature in ' + str(decoded['name']) + ', ' + str(decoded['sys']['country']) + ': ' + str(decoded['main']['temp']) + ' ºC'
	    string += '\nHumidity: ' + str(decoded['main']['humidity']) + ' %\nWind speed: ' + str(decoded['wind']['speed']) + ' Km/h' + '\nAtmosferic pressure: ' + str(decoded['main']['pressure']) + ' mBar'
	    if str(decoded['weather'][0]['main']) == 'Clear':
	       string += ' ☀'
	    elif str(decoded['weather'][0]['main']) == 'Clouds':
               string += ' ☁☁'
	    elif str(decoded['weather'][0]['main']) == 'Rain':
               string += ' ☔'
	    elif str(decoded['weather'][0]['main']) == 'Thunderstorm':
               string += ' ☔☔☔☔'
	    return string
         except Exception as e:
            logging.error(str(e))
      else:
        return 'Syntax error: weather location,<country>'
