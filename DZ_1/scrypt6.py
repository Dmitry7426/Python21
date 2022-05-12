# Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
# часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент
# времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.

hourOne, minuteOne, secondOne = int(input('Сколько часов - ')),  \
          int(input('минут - ')), \
          int(input('секунд - '))
hourTwo, minuteTwo, secondTwo = int(input('Сколько часов - ')),  \
          int(input('минут - ')), \
          int(input('секунд - '))
secondOneTotal = hourOne * 3600 + minuteOne * 60 + secondOne
secondTwoTotal = hourTwo * 3600 + minuteTwo * 60 + secondTwo
result = secondTwoTotal - secondOneTotal
print(result)