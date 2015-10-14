import urllib2

def execute(text):
   a = text.split()
   if a[0].lower() == 'translate':
      if len(a) > 3:
         if (a[1].__len__() == 2 or a[1] == "auto") and a[2].__len__() == 2:
            agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
            before_trans = 'class="t0">'
            link = 'http://translate.google.com/m?hl=%s&sl=%s&q=%s' % (a[2].lower(), a[1].lower(), ' '.join(a[3:len(a)]).replace(' ', '+'))
            request = urllib2.Request(link, headers=agents)
            page = urllib2.urlopen(request).read()
            translation = page[page.find(before_trans)+len(before_trans):]
            translation = translation.split("<")[0]     
	    return translation.decode('utf-8')
         else:
            return 'Argument error. Syntax: translate baseLang/auto targetLang string'
