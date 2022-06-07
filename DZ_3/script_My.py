# подсчитать сумму цифр и количество цифр
# a = 0
# c = 0
# e = 0
# for n in (input().split()):
#     c += int(n)
#     e = int(c) / int(n)
#     a += 1
# print(e, '  ', c, ' ', a)

from typing import List
# e = 0
# a = [[2, 2],[2, 1]]
# b = [[1, 2],[2, 1]]
# e = a + b
# print(a[0][0] + b[1][0])
def stops():
    print('Стоп!')
    exit()
def calc():
    speed1 = int(input('Введите скорость: '))
    price = int(input('Введите цену на бензин: '))
    distance = 3000
    expend1 = 5
    expend2 = 6
    expend3 = 7
    expend4 = 8
    while speed1 > 50 and speed1 < 130:
        if speed1 <= 80:
            sum_fuel = (distance * expend1) / 100
        if speed1 > 80 and speed1 <= 90:
            sum_fuel = (distance * expend2) / 100
        if speed1 > 90 and speed1 <= 100:
            sum_fuel = (distance * expend3) / 100
        if speed1 > 100 and speed1 <= 120:
            sum_fuel = (distance * expend4) / 100
        sum_price = sum_fuel * price
        print('При скорости ' + str(speed1) + ' км/ч потребуется '
              + str(sum_fuel) + ' литров топлива! На это потребуется '
              + str(sum_price) + ' рублей при цене топлива ' + str(price))
        calc()
    else:
        print('Значение скорости вне диапазона!')
        stops()
# break
calc()


    # print('Значение скорости вне диапазона!')

# sum_price = sum_fuel * price
# print('При скорости ' + str(speed1) + ' км/ч потребуется ' + str(sum_fuel) + ' литров топлива! На это потребуется ' + str(sum_price) + ' рублей при цене топлива ' + str(price))

# calc()