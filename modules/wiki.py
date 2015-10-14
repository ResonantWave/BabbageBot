import wikipedia
def execute(query): 
   a = query.split()
   if a[0].lower() == 'wiki':
      if len(a) > 1:
         try:
            data = wikipedia.summary(' '.join(a[1:len(a)]), sentences=4).decode('utf-8')
         except wikipedia.exceptions.DisambiguationError as e:
            data = ('Multiple pages found:\n' + ', '.join(e.options)).decode('utf-8')
         except wikipedia.exceptions.PageError:
            data = 'Error: Page not found.'
         return data
      else:
         return 'Syntax error: wiki topic'
