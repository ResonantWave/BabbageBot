# -*- coding: utf-8 -*- 
import sys
import re
import urllib2
import json
import subprocess
import time
import wikipedia
import logging
import os
from websocket import create_connection

## COMMAND IMPORTS
import modules.translate as translate
import modules.wiki as wiki
import modules.weather as weather
##


TOKEN = "" # YOUR SLACK API KEY GOES HERE
TOKEN = os.environ['TOKEN'] # DELETE THIS


reload(sys)
sys.setdefaultencoding('utf8')

wikipedia.set_lang('en')
data = urllib2.urlopen("https://slack.com/api/rtm.start?token=" + TOKEN)
result = data.read()

jsonDecoded = json.loads(result)

print str(jsonDecoded['ok']) + ": " + jsonDecoded['self']['name']

ws = create_connection(jsonDecoded['url'])

def send(channel, text, type = 'message', id = '1'):
   ws.send(json.dumps({'type' : type, 'channel': channel, 'text': text, 'id': id}))

while True:
   result = json.loads(ws.recv())
   try:
      if result['type'] == "message":
         if result['text'].lower() == "joke":
            proc = subprocess.Popen(['pyjoke'], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
	    send(result['channel'], out.replace('\n', ''))

         if result['text'].lower().find("wiki") != -1:
            send(result['channel'], wiki.execute(result['text']))

         if result['text'].lower().find("translate") != -1:
            send(result['channel'], translate.execute(result['text']))

         if result['text'].lower().find("weather") != -1:
	    send(result['channel'], weather.execute(result['text']))
      time.sleep(1)
   except KeyError:
      pass
