#
import math
n = int(input('Введите число n: '))
Fk = 1
e = 0
Fb = 0
for i in range(2, n + 1):
    Fk *= i
for i in range(1, n - 1):
    Fb += (1/(i + 1))
x = round(Fb, 2)
e += Fk / x
print(Fk)
print(Fb)
print('%.6f'%e)


