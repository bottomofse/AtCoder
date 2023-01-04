N, W = map(int, input().split(' '))
 
cnt = 0
sum_renga = W
while sum_renga <= N:
  sum_renga += W
  cnt += 1
print(cnt)