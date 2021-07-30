import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError :
    print(f'\033[31mSem acesso ao site\033[m')
else:
    print(f'\033[32mSite acessado com sucesso!!\033[m')
