from random import randint

def execute(data):
   syntaxError = 'Syntax error: rand <startNum> <endNum>'
   a = data.split()
   if a[0].lower() == 'rand':
      if len(a) == 2:
         if a[1].isdigit():
            return str(randint(0, int(a[1])))
         else:
	    return syntaxError
      elif len(a) > 2:
         if a[1].isdigit() and a[2].isdigit():
	    return str(randint(int(a[1]), int(a[2])))
         else:
	    return syntaxError
      elif len(a) == 1:
         return str(randint(0, 65535))
      else:
         return syntaxError
