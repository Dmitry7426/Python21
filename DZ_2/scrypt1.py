A, B, C = int(input('Введите три целых числа. Первое число - ')),  \
          int(input('второе число - ')), \
          int(input('третье число - '))

if A == B and A == C and B == C:
    print('3')
elif A == B or A == C or B == C:
    print('2')
else:
    print('1')
