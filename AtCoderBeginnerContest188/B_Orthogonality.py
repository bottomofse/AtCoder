N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
res = 0
for i in range(len(A)):
  res = res + A[i] * B[i]
if res == 0:
  print('Yes')
else:
  print('No')
