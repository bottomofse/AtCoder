A, B, W = map(int, input().split(' '))
W = W * 1000
 
max_kosuu = 0
min_kosuu = 10000000
 
min_weight = A
max_weight = B
cnt = 1
while min_weight <= W or max_weight <= W:
  if max_weight >= W and min_weight <= W:
    if min_kosuu > cnt:
      min_kosuu = cnt
    if max_kosuu < cnt:
      max_kosuu = cnt
  cnt += 1
  min_weight += A
  max_weight += B
if max_kosuu == 0:
  print('UNSATISFIABLE')
else:
  print(str(min_kosuu) + ' ' + str(max_kosuu))