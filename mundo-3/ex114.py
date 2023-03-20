''' Crie um código em Python que teste se o site pudim está acessível pelo computador usado. '''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except:
    print('O site está fora do ar')
else:
    print('O site está funcionando')
