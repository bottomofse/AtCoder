N = int(input())
x = 1
ans = set()
while x ** 2 <= N:
  if N % x == 0:
    ans.add(x)
    ans.add(N//x)
  x += 1
ans = list(ans)
ans.sort()
for i in ans:
  print(i)