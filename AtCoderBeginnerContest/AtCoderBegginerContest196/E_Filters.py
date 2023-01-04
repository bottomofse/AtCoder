N = int(input())

high = 1 << 60
low = -1 << 60
add = 0

for i in range(N):
  a, t = map(int, input().split())
  if t == 1:
    low += a
    high += a
    add += a
  elif t == 2:
    if low < a:
      low = a
    if high < a:
      high = a
  else:
    if low > a:
      low = a
    if high > a:
      high = a

X = input()
for i in map(int,input().split()):
  print(min(high, max(low, i + add)))
