# Дана последовательность из n целых чисел, каждое из которых находится в диапазоне от 0 до 100.
# Указать в данной последовательности количество вхождений числа, встречающегося чаще других.

n = int(input('Введите число n:  '))
a = [int(x) for x in input().split()]
q = []
for i in a:
    s = 0
    for j in a:
        if i == j:
            s += 1
    q.append(s)
max_coin = max(q)
print(max_coin)



