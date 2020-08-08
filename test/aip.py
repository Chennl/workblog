from urllib.request  import urlopen
from json import load
import sys
import chardet
import re


#'111.0.126.108'#
my_ip = load(urlopen('http://httpbin.org/ip'))['origin']
print('httpbin.org', my_ip)
#my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
#print('api.ipify.org', my_ip)


content = urlopen('http://ip.ws.126.net/ipquery?ip=%s'%(my_ip)).read().decode('gb2312')
# print(chardet.detect(content))
obj=re.search(r'lo="(.*)".*lc="(.*)";',content,re.M|re.I)
if obj:
    addr = obj.group(1)+obj.group(2)
    print(addr)
  