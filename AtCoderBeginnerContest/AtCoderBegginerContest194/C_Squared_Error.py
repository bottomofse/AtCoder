N = int(input())
data = list(map(int, input().split(' ')))
 
ans = 0
cur_sum = 0
for i in data:
  ans += (N - 1) * (i ** 2)
  ans -= 2 * i * cur_sum
  cur_sum += i
print(ans)