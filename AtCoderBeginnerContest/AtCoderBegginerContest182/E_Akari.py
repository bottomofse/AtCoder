H, W, N, M = map(int, input().split(' '))
 
#0�������Ȃ��A1�����A2���u���b�N
field_hor = [[0 for i in range(W)] for j in range(H)]
field_ver = [[0 for i in range(W)] for j in range(H)]
#�����̃��X�g
right = []
for i in range(N):
  y,x = map(int, input().split(' '))
  right.append((y - 1,x - 1))
for i in range(M):
  y,x = map(int, input().split(' '))
  field_hor[y-1][x-1] = 2
  field_ver[y-1][x-1] = 2
 
#�������̊m�F
for i in right:
  if field_hor[i[0]][i[1]] == 0:
    #�E
    for j in range(i[1], W):
      if field_hor[i[0]][j] == 2:
        break
      else:
        field_hor[i[0]][j] = 1
    #��
    for j in range(i[1], -1, -1):
      if field_hor[i[0]][j] == 2:
        break
      else:
        field_hor[i[0]][j] = 1
#�c�����̊m�F
for i in right:
  if field_ver[i[0]][i[1]] == 0:
    #��
    for j in range(i[0], H):
      if field_ver[j][i[1]] == 2:
        break
      else:
        field_ver[j][i[1]] = 1
    #��
    for j in range(i[0], -1, -1):
      if field_ver[j][i[1]] == 2:
        break
      else:
        field_ver[j][i[1]] = 1
#�J�E���g
cnt = 0
for i in range(H):
  for j in range(W):
    if (field_hor[i][j] == 1) or (field_ver[i][j] == 1):
      cnt += 1
print(cnt)
