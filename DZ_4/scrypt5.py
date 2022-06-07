#

n = int(input('Введите число n: '))
sum = 0
sum2 = 0
i = 1
for i in range(n):
    i += 1
    sum += 1/(2*i)**2
print('%.6f'%sum)

