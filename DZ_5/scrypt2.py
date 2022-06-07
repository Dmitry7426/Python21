# Дано n различных чисел. Найти среди них два числа, модуль разности которых имеет
# наименьшее значение. Вывести модуль разности.

n = int(input('Введите число n:  '))
a = [int(x) for x in input().split()]
mod1 = a[0]
mod2 = a[0]
for i in range(-1, n - 1):
    mod1 = abs(a[i] - a[i + 1])
    for i in range(-1, n - 1):
        mod2 = abs(a[i] - a[i + 1])
        if mod1 > mod2:
            mod1 = mod2
print(mod1)
