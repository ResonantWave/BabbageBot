import subprocess
import json
import os

signs = ['capricorn', 'aquarius', 'pisces', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius']

def execute(data):
   a = data.split()
   if a[0].lower() == "horoscope":
      if len(a) > 1:
         if a[1].lower() in signs:
            number = signs.index(a[1].lower())
            proc = subprocess.Popen(["curl -H \"Content-Type: application/json\" -d \"{ \\\"sign\\\": \\\"" + signs[number] + "\\\" }\" \"https://run.blockspring.com/api_v2/blocks/daily-horoscope\">>horoscope"], stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()

            f = open("horoscope", 'r')
            lines = f.read()
            f.close()
            os.remove('horoscope')
            decoded = json.loads(lines)
            result = str(decoded['horoscope'])

            return result.decode('utf-8')

         else:
            return 'Error: Invalid astrological sign. Available: Capricorn, Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius'
   else:
      return 'Syntax error: horoscope <astrological sign>'
