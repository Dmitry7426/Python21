# Подается на вход точность eps. Вычислить число e с заданной точностью
# Критерий остановки - подсчитаннгое число отличается от встроенного math.e меньше eps
#  1 + 1/1! + 1/2! + 1/3! + 1/4!........

import math
eps = float(input())
s = 0
k = 0
while abs(s - math.e) >= eps:
    s += 1/math.factorial(k)
    k += 1
print(s)





