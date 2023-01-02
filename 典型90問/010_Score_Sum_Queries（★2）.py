N = int(input())
class1 = [0 for i in range(N + 2)]
class2 = [0 for i in range(N + 2)]
for i in range(N):
  c, p = map(int, input().split(' '))
  if c == 1:
    class1[i + 1] = class1[i] + p
    class2[i + 1] = class2[i]
  else:
    class2[i + 1] = class2[i] + p
    class1[i + 1] = class1[i]
Q = int(input())
for i in range(Q):
  l, r = map(int, input().split(' '))
  print(str(class1[r] - class1[l - 1]) + ' ' + str(class2[r] - class2[l - 1]))
