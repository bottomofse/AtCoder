N = int(input())
for i in range(N):
  minimum, maximum = map(int, input().split(' '))
  #�v�Z
  #�ő�l
  a = maximum - 2 * minimum + 1
  #�ŏ��l
  b = 1
  if a < 0:
    a = 0
    b = 0
  c = int(((a + b) * (a - b + 1)) /2)
  print(c)
