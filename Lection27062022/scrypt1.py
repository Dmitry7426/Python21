# сортировка подсчетом

# n = int(input())
# a = [int(x) for x in input().split()]
# count1 = [0 for i in range(30000)]
# count2 = [0 for i in range(30000)]
# for x in a:
#     if x >= 0:
#         count1[x] += 1
#     else:
#         count2[abs(x)] += 1
#
# for i in range(1009, -1, -1):
#     for j in range(count2[i]):
#         print(-i, end=' ')
#
# for i in range(1009):
#     for j in range(count1[i]):
#         print(i, end=' ')
#

# другое решение сортировки подсчетом
# n = int(input())
# a = [int(x) for x in input().split()]
# freq = {x : 0 for x in range(-10005, 10005)}
#
# for number in a:
#     freq[number] += 1
# for key, value in freq.items():
#     for i in range(value):
#         print(key, end=' ')

