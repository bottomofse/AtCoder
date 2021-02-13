import math
N = int(input())
data = list(map(int, input().split(' ')))
 
a = 0
for i in data:
  a += abs(i)
b = 0
for i in data:
  b += (i) ** 2
#b = decimal.Decimal(b) ** (1 /2)
b = math.sqrt(b)
c = 0
for i in data:
  if abs(i) > c:
    c = abs(i)
print(a)
print('{:.15g}'.format(b))
print(c)