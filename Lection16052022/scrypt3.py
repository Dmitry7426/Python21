# подается число на вход, определить имеется ли там цифра 2

n = int(input())
res = False
while n > 0:
    if n % 10 == 2:
        res = True
        break
    n //= 10
if res:
    print('имеется')
else:
    print('не имеется')

print(n)

