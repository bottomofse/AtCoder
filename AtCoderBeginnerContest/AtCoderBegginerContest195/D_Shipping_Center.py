N, M, Q = map(int, input().split(' '))
 
nimotsu_list = []
for i in range(N):
  nimotsu_list.append(list(map(int, input().split(' '))))
#‰×•¨‚Ìƒ\[ƒg
nimotsu_list.sort(key=operator.itemgetter(0))
#print(nimotsu_list)
nimotsu_list.sort(key=operator.itemgetter(1),reverse=True)
#print(nimotsu_list)
 
hako_list = list(map(int, input().split(' ')))
#print(hako_list)
 
max_score = 0
for i in range(Q):
  score = 0
  #‘ÎÛ‹æŠÔ
  L, R = map(int, input().split(' '))
  queried_hako_list = copy.deepcopy(hako_list[:L - 1] + hako_list[R:])
  queried_hako_list.sort()
  
  for j in nimotsu_list:
    ookisa = j[0]
    kachi = j[1]
    index = 0
    for k in range(len(queried_hako_list)):
      if ookisa <= queried_hako_list[index]:
        break
      index += 1
    if index != len(queried_hako_list):
      score += kachi
      queried_hako_list.pop(index)
  print(score)
  #print(queried_hako_list)