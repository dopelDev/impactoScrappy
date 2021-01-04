from bs4 import BeautifulSoup
import re

# regex
group = r'https://www.impacto.com.pe/'
group1 = r'(catalogo\?categoria=.*)'
regex1 = re.compile(group + group1)

pathOfHtml = '/home/dopel/projects/impactoScrappy'
objFile = open(pathOfHtml + '/assets/impacto.html')
sopa = BeautifulSoup(objFile.read(), 'html.parser')

listOfUrl = []
for url in sopa.find_all('a'):
    if url.get('href') is None:
        continue
    else:
        tmp = url.get('href')
        if regex1.search(tmp):
            listOfUrl.append(url.get('href'))

for index, url in enumerate(listOfUrl):
    print(index, '\t', url)
