import itertools
 
N, K = map(int, input().split(' '))
 
cost = []
for i in range(N):
  cost.append(list(map(int, input().split(' '))))
 
kumiawase = [(i + 1) for i in range(N - 1)]
cnt = 0
for i in itertools.permutations(kumiawase):
  test = [0] + list(i) + [0]
  sum_dis = 0
  for j in range(len(test) - 1):
    sum_dis += cost[test[j]][test[j + 1]]
  if sum_dis == K:
    cnt += 1
print(cnt)
