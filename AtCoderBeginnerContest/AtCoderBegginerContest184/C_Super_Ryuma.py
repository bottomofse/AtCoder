a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))
if a == c and b == d:
  print(0)
  exit()
if a + b == c + d:
  print(1)
  exit()
if a - b == c - d:
  print(1)
  exit()
if abs(a - c) + abs(b - d) <= 3:
  print(1)
  exit()
if (a + b) % 2 == (c + d) % 2: