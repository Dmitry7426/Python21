# Даны два целых числа a и b. Найти сумму квадратов чисел от a до b включительно.

a = float(input('Введите вещественное число А: '))
n = int(input('Введите целое число n: '))
sum = 1
sum2 = 0
i = 1
for i in range(n):
    i += 1
    if i % 2 == 0:
        sum += a**i
    else:
        sum -= a**i
print('%.3f'%sum)

