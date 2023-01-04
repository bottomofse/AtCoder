N = int(input())
data = [0 for _ in range(N+1)]
res = 0
for i in range(1, N+1):
   for j in range(i, N+1, i):
       data[j] += 1
for i, cnt in enumerate(data): res += i*cnt
print(res)
