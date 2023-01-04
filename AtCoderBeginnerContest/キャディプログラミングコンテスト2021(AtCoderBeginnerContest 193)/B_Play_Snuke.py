N = int(input())
 
min_price = 10000000000
for i in range(N):
  A, P, X = map(int, input().split(' '))
  if X > A and P < min_price:
    min_price = P
if min_price == 10000000000:
  print(-1)
else:
  print(min_price)