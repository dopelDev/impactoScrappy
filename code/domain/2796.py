from bs4 import BeautifulSoup

# paths
pathOfHtml = '/home/dopel/projects/impactoScrappy'
objFile = open(pathOfHtml + '/assets/impacto.html')
sopa = BeautifulSoup(objFile.read(), 'html.parser')
count = 0
validUrls = 0
listOfUrl = []
listOut = []
for url in sopa.find_all('a'):
    listOfUrl.append(url.get('href'))
domainName = listOfUrl[0]    # el domain
print(domainName, 'this is domain')

for url in listOfUrl:
    # no verifica la lista si hay Nones
    if url is None:
        continue
    else:
        if domainName in url:
            if url == domainName:
                continue
            elif 'page' in url:
                continue
            elif 'login' in url:
                continue
            else:
                listOut.append(url)
lenght = len(listOut)
objFile2 = open('/home/dopel/projects/impactoScrappy/scrappyData/domainUrls.txt', mode='w')
for line in range(len(listOut)):
    if line < len(listOut) - 1:
        objFile2.writelines(listOut[line])
        objFile2.writelines('\n')
    else:
        objFile2.writelines(listOut[line])
objFile2.close()
