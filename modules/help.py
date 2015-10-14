import list

def execute(data):
   a = data.split()
   if a[0].lower() == 'help':
      commandList = ''
      for key in list.commandModules.keys():
         commandList += key + ', '
      return 'Available modules: ' + commandList[:-2] + '.' # the :-2 should remove the ', '
