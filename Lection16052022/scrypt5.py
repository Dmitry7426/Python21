x, eps = map(float, input().split())
prev_sum = 0
cur_sum = x
k = 2 # степень х и знаменатель
while abs(cur_sum - prev_sum) >= eps:
    prev_sum = cur_sum
    term = x ** k / k
    if k % 2 == 0:
        term *= -1
    cur_sum += term
    k += 1
print(cur_sum)