N = int(input())
data = list(map(int, input().split(' ')))
cnt = 0
for i in range(N):
  if (i + 1) % 2 == 1 and data[i] % 2 == 1:
    cnt += 1
print(cnt)