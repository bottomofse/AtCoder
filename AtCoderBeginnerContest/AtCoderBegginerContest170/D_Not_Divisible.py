N = int(input())
data = list(map(int, input().split(' ')))
data.sort()
data_max = data[-1]
a = [0 for i in range(data_max + 1)]
b = [False for i in range(data_max + 1)]
for i in data:
  a[i] += 1
  if b[i]:
    continue
  for j in range(2, len(b)):
    if i * j >= len(b):
      break
    b[i * j] = True 
cnt = 0
for i in data:
  if a[i] == 1 and not b[i]:
    cnt += 1
print(cnt)