X = input()
str_M = input()
M = int(str_M)
d = int(max(list(X)))
 
#指定した進数表現の数値を10進数にして返す
def transfer(str_number, n):
  ret = 0
  kisuu = 1
  tmp_list = list(str_number)
  for i in range(len(tmp_list) - 1, -1, -1):
    ret += int(tmp_list[i]) * kisuu
    kisuu = kisuu * n
  return ret
 
if len(X) < 2:
  a = M - int(X)
  if a >= 0:
  	print(1)
  else:
    print(0)
  exit()
 
max_sinsuu = 0
left = d
right = M + 1
mid = (left + right) // 2
#print(mid)
while left <= right:
  #if mid == 0:
  #  break
  tmp = transfer(X, mid)
  if tmp <= M:
    if transfer(X, mid + 1) > M:
      max_sinsuu = mid
      break
    else:
      mid = mid + 1
    left = mid
  else:
    if transfer(X, mid - 1) <= M:
      max_sinsuu = mid - 1
      break
    else:
      mid = mid - 1
    right = mid
  mid = (left + right) // 2
ans = max_sinsuu - d
if ans > 0:
  print(ans)
else:
  print(0)