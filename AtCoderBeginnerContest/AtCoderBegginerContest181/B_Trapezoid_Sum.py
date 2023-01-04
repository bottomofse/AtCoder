N = int(input())
 
sum_num = 0
for i in range(N):
  a, b = map(int,input().split(' '))
  sum_num += int((a + b) * (b - a + 1) * (1/2))
print(sum_num)
