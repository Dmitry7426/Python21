# N белочек нашли K орешков и решили разделить их поровну.
# Определите, сколько орешков достанется каждой белочке.

N = int(input('Введите сколько белочек? - '))
K = int(input('Введите сколько орешков всего? - '))
print('Каждой белочке достанется по ' + str(K // N) + ' орешка!')
