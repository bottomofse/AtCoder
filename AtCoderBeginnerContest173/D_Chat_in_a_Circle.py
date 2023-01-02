A = int(input())
data = list(map(int, input().split(' ')))
data.sort(reverse=True)
index = 1
cnt = data[0]
for i in range(2, A):
  cnt += data[index]
  index = index + 1 if i %2 == 1 else index
print(cnt)
