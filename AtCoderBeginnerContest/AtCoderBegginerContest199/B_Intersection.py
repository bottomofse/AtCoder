N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
 
cnt_list = [True for i in range(1001)]
maximum = 1000
minimum = 0
 
for i in range(N):
  next_cnt_list = [False for i in range(1001)]
  up = 0
  low = 0
  if A[i] > B[i]:
    up = A[i]
    low = B[i]
  else:
    up = B[i]
    low = A[i]
  for i in range(low, up + 1):
    if cnt_list[i] == True:
      next_cnt_list[i] = True
  cnt_list = next_cnt_list
cnt = 0
for i in cnt_list:
  if i:
    cnt += 1
print(cnt)