import re
import unicodedata
import codecs
def findWord(f):
    wrFile = codecs.open('c:/pythonWeb21/DZ_Dict_Files/answer.txt', 'w', 'UTF-8')
    readFile = f.read().lower()
    norma = unicodedata.normalize('NFKD', readFile)
    # only_asc = norma.encode('ASCII', 'ignore')
    # content = re.sub(r'[0-9, a-z, ?,.~@#$%^&*(),''<>/!^~]', " ", norma)
    content = re.sub(r'[\Wa-z0-9]', " ", norma)
    freq = {}
    for word in content.split():
        if word in freq:
            freq.update({word: freq[word] + 1})
        else:
            freq.update({word: 1})
    for key, value in freq.items():
        wrFile.write('Слово {} встречается {} раз\n'.format(key, value))
    wrFile.close()

with open('c:/pythonWeb21/DZ_Dict_Files/war and peace.txt', 'r', encoding='utf8', errors='replace') as f:
    findWord(f)


