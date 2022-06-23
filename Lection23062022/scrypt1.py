  # словари

# n = int(input())
# frequency = {}
# for i in range(n):
#     word = input()
#     if word not in frequency:
#         # добавляемп новое слово в словарь с частотой 1
#         frequency.update({word : 1})
#     else:
#         # увеличиваем частоту данного слова на 1
#         frequency.update({word : frequency[word] + 1})
#
# for key, value in frequency.items():
#     print('Слово {} встречается {} раз'.format((key, value)))
#

# text = input()
# frequency = {}
# for word in text.split():
#     if word in frequency:
#         frequency.update({word : frequency[word] + 1})
#     else:
#         frequency.update({word : 1})
# for key, value in frequency.items():
#     print('Слово {} встречается {} раз'.format(key, value))
#


  # Работа с файлами

import random
#
# f = open('c:/python21/test.txt', 'a+')
# f.write('Тест записи файла\n')
# for i in range(100000000):
#     num = random.randint(1, 10000)
#     f.write(f'{i}\n')
#
# f.close()

   # Через рекурсию

# alf = '1234'

# for c1 in alf:
#     for c2 in alf:
#         for c3 in alf:
#             print(c1 + c2 + c3)
# функция добавляет в с троку все символы с номерами от старт до енд (в кодировке)
# def addSymbols(str, start, end):
#     start = ord(start)
#     end = ord(end)
#     while start <= end:
#         str += chr(start)
#         start += 1
#     return str
#
# alph = addSymbols('', 'a', 'z')
# alph = addSymbols(alph, 'A', 'Z')
# alph = addSymbols(alph, '0', '9')
#
# print(alph)
# # функция генерации всех паролей из алфавита alph в файл f
# def generate(alph, n, f, curentPassword):
#     if len(curentPassword) == n:
#         f.write(curentPassword + '\n')
#         return
#     for c in alph:
#         generate(alph, n, f, curentPassword + c)
#
# f = open('c:/python21/text.txt', 'w')
# generate(alph, 5, f, '')

# def slova(f):

def slova(f):
    wr = open('c:/python21/text2.txt', 'w')
    a = f.read()
    frequency = {}
    for word in a.split():
        if word in frequency:
            frequency.update({word : frequency[word] + 1})
        else:
            frequency.update({word : 1})
    for key, value in frequency.items():
        wr.write('Слово {} встречается {} раз\n'.format(key, value))
    wr.close()

f = open('c:/python21/text.txt', 'r')
slova(f)
f.close()


