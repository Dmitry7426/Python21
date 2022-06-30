# n = int(input())
# a = [int(x) for x in input().split()]
# s = 1
# for i in range(0, n - 1):
#     if a[i] != a[i + 1]:
#         s += 1
# print(s)
#



# n = int(input())
# a = [int(x) for x in input().split()]
# for i in range(0, n - 1):
#     if i > a[i + 1]:
#         print(i + 1)
#         break
#     elif i == len(a) - 1:
#         print(len(a) + 1)


# n1, n2, st = int(input()), int(input()), input()
# if st == '+':
#     print(n1 + n2)
# if st == '-':
#     print(n1 - n2)
# if st == '*':
#     print(n1 * n2)
# if st == '/':
#     if n2 == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(n1 / n2)
# else:
#     print('Неверная операция')

# st1, st2 = str(input()), str(input())
# if st1 in ('красный', 'синий', 'желтый') and st2 in ('красный', 'синий', 'желтый'):
#     if st1 == st2:
#         print('ошибка цвета')
#     if st1 == 'красный' and st2 == 'синий' or st2 == 'красный' and st1 == 'синий':
#         print('фиолетовый')
#     if st1 == 'красный' and st2 == 'желтый' or st2 == 'красный' and st1 == 'желтый':
#         print('оранжевый')
#     if st1 == 'желтый' and st2 == 'синий' or st2 == 'желтый' and st1 == 'синий':
#         print('зеленый')
# else:
#     print('ошибка цвета')
# n = int(input())
# black = 'чёрный'
# red = 'красный'
# if n >= 0 and n <= 36:
#     if n == 0:
#         print('зеленый')
#     if n >= 1 and n <= 10:
#         if n % 2 == 0:
#             print(black)
#         else:
#             print(red)
#     if n >= 11 and n <= 18:
#         if n % 2 == 0:
#             print(red)
#         else:
#             print(black)
#     if n >= 19 and n <= 28:
#         if n % 2 == 0:
#             print(black)
#         else:
#             print(red)
#     if n >= 29 and n <= 36:
#         if n % 2 == 0:
#             print(red)
#         else:
#             print(black)
# else:
#     print('Число вне диапазона')



# a1, a2 , b1, b2 = int(input()), int(input()), int(input()), int(input())
for i in range(1, 9):
    a1 = i
    for j in range(1, 9):
        a2 = j
        for k in range(1, 9):
            b1 = k
            for y in range(1, 9):
                b2 = y

                black1 = 'black'
                black2 = 'black'
                grey1 = 'grey'
                grey2 = 'black'
                e1 = ''
                e2 = ''
                if (a1 + a2) % 2 == 0:
                    e1 = grey1
                else:
                    e1 = black1
                if (b1 + b2) % 2 == 0:
                    e2 = grey1
                else:
                    e2 = black1
                if e1 == e2:
                    print(a1, a2, b1, b2, 'цвета одинаковые')
                else:
                    print(a1, a2, b1, b2, 'цвета разные')


