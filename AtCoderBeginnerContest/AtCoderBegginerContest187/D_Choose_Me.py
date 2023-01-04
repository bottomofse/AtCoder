N = int(input())
 
X = 0
score_list = []
for i in range(N):
  A, B = map(int, input().split(' '))
  X -= A
  score_list.append(2 * A + B)
score_list.sort()
cnt = 0
while X <= 0:
  X += score_list.pop()
  cnt += 1
print(cnt)
