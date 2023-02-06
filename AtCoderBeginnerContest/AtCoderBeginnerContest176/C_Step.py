N = int(input())
data = list(map(int, input().split(' ')))
 
max_tall = data[0]
result = 0
for i in range(1, N):
  if max_tall >= data[i]:
    result += max_tall - data[i]
  else:
    max_tall = data[i]
print(result)