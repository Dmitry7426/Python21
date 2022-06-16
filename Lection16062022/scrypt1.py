# Является ли строка палиндромом

# def isPalindrome(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         if s[i] !=s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
#
# string = ['abab', '123321', 'aaa']
# for s in string:
#     if isPalindrome(s):
#         print('Строка {} палиндром'.format(s))
#     else:
#         print('Строка {} не палиндром'.format(s))

def vYears(year):
    if year%400 == 0 or year%4 == 0 and year/100 != 0:
        return False
    return True

def errYear(year):

    if isinstance(year, int) and year >= 0:
        return True
    return False


def nextViYear(s):
    for i in range(s, 5):
        if s % 400 == 0 or s % 4 == 0 and s / 100 != 0:
            print('Следующий високосный год будет {}'.format(s))

year = int(input('Введите год:  '))

if errYear(year):
    if vYears(year):
        print('Год {} вискосный!'.format(vYears()))
    else:
        print('Год {} не вискосный!'.format(vYears()))





# nextViYear(year)

def allVisYear(s1, s2):
    for i in range(s1, s2):
        if i % 400 == 0 or i % 4 == 0 and i / 100 != 0:
            print(i)

# year1 = int(input('Введите год от - '))
# year2 = int(input('Введите год до - '))
# allVisYear(year1, year2)
