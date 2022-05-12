# import math
# a = float(input())
# b = float(input())
# c = float(input())
# p = (a + b + c) / 2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)

# a, b ,c = float(input('сторона а - ')), float(input('сторона b - ')), float(input('сторона c - '))
#
# if a < b + c and b < a + c and c < a + b:
#     print('Треугольник может быть построен!')
# else:
#     print('Треугольник не может быть построен!')

# a, b ,c = float(input('сторона а - ')), float(input('сторона b - ')), float(input('сторона c - '))
# res = 0
# if a < b + c and b < a + c and c < a + b:
#     print('Треугольник может быть построен!')
#     res = 1
# if res == 1:
#     if a == b and a == c and b == c:
#         print('Треугольник равносторонний')
#     elif a == b or b == c or a == c:
#         print('Треугольник равнобедренный')
#     else:
#         print('Разносторонний')
# else:
#     print('Треугольник не может быть построен!')

# import math
#
# A, B ,C = float(input('A - ')), float(input('B - ')), float(input('C - '))
# D = B**2-4*(A*C)
# if D > 0:
#     X1 = (-B + math.sqrt(D))/(2*A)
#     X2 = (-B - math.sqrt(D)) / (2 * A)
#     print('два корня: ' + str(X1) + ' и ' + str(X2))
# if D == 0:
#     X1 = (-B + math.sqrt(D)) / (2 * A)
#     print('один корень: ' + str(X1))
# if D < 0:
#     print('NO SOLUTION')

# N = int(input('Введите четырехзначное число: '))
# one = N // 100
# one1 = one // 10
# one2 = one % 10
# oneSum = one1 + one2
# two = N % 100
# two1 = two // 10
# two2 = two % 10
# twoSum = two1 + two2
#
# if oneSum == twoSum:
#     print('Число счастливое')
# else:
#     print('Число не счастливое')

x0 = 0
y0 = 0
R = 5
x = int(input('Введите X - '))
y = int(input('Введите Y - '))
if (((x - x0)**2) + ((y - y0)**2)) <= R**2:
    print('Точка лежит в круге')
else:
    print('Точка не в круге')
