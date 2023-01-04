H, W, N, M = map(int, input().split(' '))
 
#0が何もない、1が光、2がブロック
field_hor = [[0 for i in range(W)] for j in range(H)]
field_ver = [[0 for i in range(W)] for j in range(H)]
#光源のリスト
right = []
for i in range(N):
  y,x = map(int, input().split(' '))
  right.append((y - 1,x - 1))
for i in range(M):
  y,x = map(int, input().split(' '))
  field_hor[y-1][x-1] = 2
  field_ver[y-1][x-1] = 2
 
#横方向の確認
for i in right:
  if field_hor[i[0]][i[1]] == 0:
    #右
    for j in range(i[1], W):
      if field_hor[i[0]][j] == 2:
        break
      else:
        field_hor[i[0]][j] = 1
    #左
    for j in range(i[1], -1, -1):
      if field_hor[i[0]][j] == 2:
        break
      else:
        field_hor[i[0]][j] = 1
#縦方向の確認
for i in right:
  if field_ver[i[0]][i[1]] == 0:
    #下
    for j in range(i[0], H):
      if field_ver[j][i[1]] == 2:
        break
      else:
        field_ver[j][i[1]] = 1
    #上
    for j in range(i[0], -1, -1):
      if field_ver[j][i[1]] == 2:
        break
      else:
        field_ver[j][i[1]] = 1
#カウント
cnt = 0
for i in range(H):
  for j in range(W):
    if (field_hor[i][j] == 1) or (field_ver[i][j] == 1):
      cnt += 1
print(cnt)
