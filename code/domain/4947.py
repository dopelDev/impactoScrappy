# aun no se
dato_path = '/home/dopel/projects/impactoScrappy/scrappyData'
objFile_clean_words = open(dato_path + '/clean_list_first_words.txt', mode='r')
clean_list_first_words = []
count = 0
for line in objFile_clean_words.readlines():
    count += 1
    if line == '' or line == '\n':
        continue
    else:
        clean_list_first_words.append(line.replace('\n', ''))
# print(clean_list_first_words)
print(len(clean_list_first_words))
print(count)
objFile_clean_words.close()
