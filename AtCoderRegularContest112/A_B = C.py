N = int(input())
for i in range(N):
  minimum, maximum = map(int, input().split(' '))
  #計算
  #最大値
  a = maximum - 2 * minimum + 1
  #最小値
  b = 1
  if a < 0:
    a = 0
    b = 0
  c = int(((a + b) * (a - b + 1)) /2)
  print(c)
