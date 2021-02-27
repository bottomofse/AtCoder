N = int(input())
 
memo = {}
for i in range(2, 100001):
  flg = False
  if i in memo:
    continue
  for j in range(2, 36):
    tmp = i ** j
    if tmp <= N:
      memo[tmp] = 1
      continue
    elif j == 2:
      flg = True
    break
  if flg:
    break
print(N - len(memo))