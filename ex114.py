import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://front-labo.herokuapp.com/dashboard')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso.')
