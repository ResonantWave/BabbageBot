import urllib2
import json
import math

def execute(data):
   latitude = 42.0  # Change to your location
   longitude = -8.0 # Change to your location
   R = 6378 # Earth's radius
   try:
      response = urllib2.urlopen('https://api.wheretheiss.at/v1/satellites/25544')
      html = response.read()
      decoded = json.loads(html)
   except Exception:
      outgoingMessageProtocolEntity = TextMessageProtocolEntity(
      'Unknown error',  # Because we're lazy, aren't we?
      to = messageProtocolEntity.getFrom())
      self.toLower(outgoingMessageProtocolEntity)
   dLat = math.radians(decoded['latitude'] - latitude)
   dLon = math.radians(decoded['longitude'] - longitude)

   a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(latitude)) * \
       math.cos(math.radians(decoded['latitude'])) * math.sin(dLon/2) * \
       math.sin(dLon/2)

   c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
   d = R * c

   return 'Distance to ISS: ' + str(d) + ' Km \n\nSpeed: ' + str(decoded['velocity']) + ' Km/h'
