# -*- coding: utf-8 -*- 
from __future__ import print_function

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
TOKEN = "" # YOUR SLACK API KEY GOES HERE (or as TOKEN env variable)
TOKEN = os.environ.get('TOKEN', TOKEN)
#########################################

reload(sys)
sys.setdefaultencoding('utf8')

wikipedia.set_lang('en')
try:
   data = urllib2.urlopen("https://slack.com/api/rtm.start?token=" + TOKEN)
except urllib2.URLError as exception:
   print('Error: Name or service not known. Please check your internet conectivity.')
result = data.read()

jsonDecoded = json.loads(result)

if not jsonDecoded['ok']:
   print("Error when communicating with Slack.\nReason: %s" % jsonDecoded['error'])
   sys.exit(1)

print(str(jsonDecoded['ok']) + ": " + jsonDecoded['self']['name'])

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
