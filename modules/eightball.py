from random import randint

responses = ['Definitely', 'Undoubtedly yes', 'No doubt', 'Definitely yes', 'As I see it, yes', 'Most likely', 'Yes', 
             'Everything is pointing to yes', 'No', 'The answer is no', 'Affirmative', 'Negative', 'Disgracefully, no', 
             'Unfortunately not', 'My sources say no', 'Not very likely']
def execute(data):
   a = data.split()
   if a[0].lower() == '8ball':
      if len(a) > 1:
         return responses[randint(0, len(responses)-1)]
      else:
         return 'Syntax error: 8ball <question>'
