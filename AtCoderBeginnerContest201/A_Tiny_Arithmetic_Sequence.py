data = list(map(int, input().split(' ')))
data.sort()
 
if data[0] - data[1] == data[1] - data[2]:
  print('Yes')
else:
  print('No')