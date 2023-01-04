X, N = map(int, input().split(' '))
 
if N == 0:
  print(X)
  exit()
 
data= list(map(int, input().split(' ')))
data.sort()
 
result = 0
minimum = 10000
for i in range(-100, 102, 1):
  if i in data:
    continue
  distance = abs(X - i)
  if distance < minimum:
    minimum = distance
    result = i
print(result)
