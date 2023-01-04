N = int(input())
 
min_A = 10 ** 5
min_B = 10 ** 5
min_AplusB = 10 ** 5
 
AB_list = []
for i in range(N):
  Ai, Bi = map(int, input().split(' '))
  AB_list.append([Ai, Bi])
  if min_AplusB > Ai + Bi:
    min_AplusB = Ai + Bi
#print(min_AplusB)
#print(AB_list)
min_hitori = 10 ** 5
for i in range(N):
  #A
  for j in range(i + 1, N):
    #B
    tmp = max([AB_list[i][0], AB_list[j][1]])
    #print(tmp)
    if tmp < min_hitori:
      min_hitori = tmp
for i in range(N):
  #A
  for j in range(i + 1, N):
    #B
    tmp = max([AB_list[i][1], AB_list[j][0]])
    if tmp < min_hitori:
      min_hitori = tmp
if min_hitori < min_AplusB:
  print(min_hitori)
else:
  print(min_AplusB)