import re
from alive_progress import alive_bar
from time import sleep
# regex __init__
domainName = r'https://www.impacto.com.pe/'
first_word = r'((\w+.*){,6})'
regex = re.compile(domainName + first_word)
# call list txt
pathOftxt = '/home/dopel/projects/impactoScrappy/scrappyData/'
objFile = open(pathOftxt + 'domainUrls.txt', mode='r')
listOfUrl = objFile.read()
objFile.close()
# listasd adicionales
list_first_words = []
clean_list_first_words = []
# coding
count = 0
objInter = regex.finditer(listOfUrl)
with alive_bar(manual=True) as bar:
    for item in objInter:
        list_first_words.append(item.group(1))
        print('full URL : ' + item.group(0))
        print('group 1 : ' + item.group(1))
        sleep(0.5)
        item = len(list_first_words) / 100
        bar(item)
clean_list_first_words = list(set(list_first_words))
print(len(list_first_words))
print(len(clean_list_first_words))
objFileCleanListFirstWords = open(pathOftxt + 'clean_list_first_words.txt', mode='w')
for line in range(len(clean_list_first_words)):
    if line < len(clean_list_first_words) - 1:
        objFileCleanListFirstWords.writelines(clean_list_first_words[line])
        objFileCleanListFirstWords.writelines('\n')
    else:
        objFileCleanListFirstWords.writelines(clean_list_first_words[line])
