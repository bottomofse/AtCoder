import copy
 
N, M = map(int, input().split(' '))
jouken = []
for i in range(M):
  jouken.append(list(map(int, input().split(' '))))
 
K = int(input())
ball_list = [{}]
for i in range(K):
  C, D = map(int, input().split(' '))
  next_ball_list = []
  for j in ball_list:
    tmp = copy.deepcopy(j)
    tmp[C] = 1
    next_ball_list.append(tmp)
    tmp = copy.deepcopy(j)
    tmp[D] = 1
    next_ball_list.append(tmp)
    ball_list = next_ball_list
#print(ball_list)
#print(jouken)
 
max_cnt = 0
for i in ball_list:
  cnt = 0
  for j in jouken:
    if (j[0] in i) and (j[1] in i):
      cnt += 1
  if cnt > max_cnt:
    max_cnt = cnt
print(max_cnt)