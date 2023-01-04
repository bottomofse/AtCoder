N = int(input())
res = 0
for i in range(1, N + 1):
  n = N // i
  res += n * (2 * i + (n - 1) * i) // 2
print(res)
