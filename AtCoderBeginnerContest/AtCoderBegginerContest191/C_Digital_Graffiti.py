H, W = map(int, input().split(' '))
field = []
for i in range(H):
  field.append(list(input()))
corner = 0
for i in range(1, H -1):
  for j in range(1, W - 1):
    #ブロックの場合
    if field[i][j] == '#':
      #左上
      if (field[i][j-1] == '.') and (field[i-1][j] == '.') and (field[i-1][j-1] == '.'):
        corner += 1
      #右上
      if (field[i][j+1] == '.') and (field[i-1][j] == '.') and (field[i-1][j+1] == '.'):
        corner += 1
      #左下
      if (field[i][j-1] == '.') and (field[i+1][j] == '.') and (field[i+1][j-1] == '.'):
        corner += 1
      #右下
      if (field[i][j+1] == '.') and (field[i+1][j] == '.') and (field[i+1][j+1] == '.'):
        corner += 1     
      #左上
      if (field[i][j-1] == '#') and (field[i-1][j] == '#') and (field[i-1][j-1] == '.'):
        corner += 1
      #右上
      if (field[i][j+1] == '#') and (field[i-1][j] == '#') and (field[i-1][j+1] == '.'):
        corner += 1
      #左下
      if (field[i][j-1] == '#') and (field[i+1][j] == '#') and (field[i+1][j-1] == '.'):
        corner += 1
      #右下
      if (field[i][j+1] == '#') and (field[i+1][j] == '#') and (field[i+1][j+1] == '.'):
        corner += 1      
print(corner)
