N = int(input())
sankasya = list(map(int, input().split(' ')))
sankasya_score_id = {}
for i in range(len(sankasya)):
  sankasya_score_id[sankasya[i]] = i + 1
 
#print(sankasya)
 
while True:
  if len(sankasya) == 2:
    C = sankasya[0]
    D = sankasya[1]
    if C <= D:
      print(sankasya_score_id[C])
    else:
      print(sankasya_score_id[D])
    exit()
  next_sankasya = []
  for i in range(int(len(sankasya) / 2)):
    A = sankasya[2 * i]
    B = sankasya[2 * i + 1]
    if A >= B:
      next_sankasya.append(A)
    else:
      next_sankasya.append(B)
  sankasya = next_sankasya
