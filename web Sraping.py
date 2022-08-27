import requests
from bs4 import BeautifulSoup as bs

git_user = input('Coloque seu GitHub User:')
url = 'http://github.com/' + git_user
rq = requests.get(url)
soup = bs(rq.content, "html.parser")
profile_imagem = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_imagem)
