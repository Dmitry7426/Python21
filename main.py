N = int(input())
e = 0
f = 100
while N - f > 0:
    e += N ** 2
    N -= 1
print(e)
