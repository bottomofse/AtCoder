H, W, K = map(int, input().split(' '))

field = []
black_location_list = []
for i in range(H):
  tmp = list(input())
  for j in range(W):
    if tmp[j] == '#':
      #x軸, y軸
      black_location_list.append([j, i])
  field.append(tmp)

#bit全探索
H_list = []
for bit in range(1 << H):
  comb = []
  for i in range(H):
    if bit & (1 << i):
      comb.append(i)
  H_list.append(comb)
W_list = []
for bit in range(1 << W):
  comb = []
  for i in range(W):
    if bit & (1 << i):
      comb.append(i)
  W_list.append(comb)
#print(H_list)
#print(W_list)
#print(black_location_list)

res = 0
#黒のカウント
for i in H_list:
  for j in W_list:
    black_cnt = 0
    for k in black_location_list:
      x = k[0]
      y = k[1]
      if (x not in j) and (y not in i):
        black_cnt += 1
    if black_cnt == K:
      res += 1
print(res)