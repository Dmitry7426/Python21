# Списки и кортежи
# обьявление списка
# a = []
# # список из 10 нолей
# a = [0] * 10
# # слияние списков
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# # кортежи (неизменяемый массив, элементы менять нельзя. но показать любой элемент можно)
# a = ()
# # или
# a = tuple()
# Методы списков
# append
# a = [1, 2, 3]
# a.append(4)
# print(a)
# дан массив. нужно сделать накопительную сумму,
# пример как надо:
# a = [1, 2, 3, 4, 5]
# b = [1, 3, 6, 10, 15]
# a = [int(x) for x in input().split()]
# for i in range(1, len(a)): # Range можно указывать певый параметр начала с чего потом до и третим параметром можно шаг указать
#
#     a[i] = a[i] + a[i-1]
#
# print(a)

# дается число N, вывести массив из N чисел Фибаноччи
# Последовательность фибаноччи задается :
# f[i] = f[1] + f[i - 1] + f[i - 2]

# N = int(input('Введиче число - '))
# a = [0] * N
# a[0] = 1
# a[1] = 1
# for i in range(2, N):
#     a[i] += a[i - 2] + a[i - 1]
# print(a)

# на вход подается массив а, и число Target. выдать 2 индекса I j что a[i] + a[j] = terget
# если таких нет - то написать чисел нет

a = [int(x) for x in input().split()]
target = int(input('Введите число - '))
first = 0
second = 0
found = False
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == int(target):
            first = a[i]
            second = a[j]
            found = True
            print(i, j)
# if found == True:
#     print(second)
#     print(first)
# else:
#     print('чисел нет')




