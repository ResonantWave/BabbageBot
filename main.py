# -*- coding: utf-8 -*- 
import sys
import re
import urllib2
import json
import time
import wikipedia
import logging
import os
import pyjokes
import modules.list as commandList

from websocket import create_connection


#########################################
TOKEN = "" # YOUR SLACK API KEY GOES HERE
TOKEN = os.environ['TOKEN'] # DELETE THIS
#########################################

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
      if result['type'] == 'message':
         if result['text'].lower() == 'joke':
	    send(result['channel'], pyjokes.get_joke())

	 if result['text'].lower().split()[0] in commandList.commandModules:
	    function = commandList.commandModules[result['text'].lower().split()[0]]
	    send(result['channel'], function.execute(result['text']))
      time.sleep(1)
   except KeyError:
      pass
