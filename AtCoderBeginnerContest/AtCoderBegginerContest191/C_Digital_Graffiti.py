H, W = map(int, input().split(' '))
field = []
for i in range(H):
  field.append(list(input()))
corner = 0
for i in range(1, H -1):
  for j in range(1, W - 1):
    #�u���b�N�̏ꍇ
    if field[i][j] == '#':
      #����
      if (field[i][j-1] == '.') and (field[i-1][j] == '.') and (field[i-1][j-1] == '.'):
        corner += 1
      #�E��
      if (field[i][j+1] == '.') and (field[i-1][j] == '.') and (field[i-1][j+1] == '.'):
        corner += 1
      #����
      if (field[i][j-1] == '.') and (field[i+1][j] == '.') and (field[i+1][j-1] == '.'):
        corner += 1
      #�E��
      if (field[i][j+1] == '.') and (field[i+1][j] == '.') and (field[i+1][j+1] == '.'):
        corner += 1     
      #����
      if (field[i][j-1] == '#') and (field[i-1][j] == '#') and (field[i-1][j-1] == '.'):
        corner += 1
      #�E��
      if (field[i][j+1] == '#') and (field[i-1][j] == '#') and (field[i-1][j+1] == '.'):
        corner += 1
      #����
      if (field[i][j-1] == '#') and (field[i+1][j] == '#') and (field[i+1][j-1] == '.'):
        corner += 1
      #�E��
      if (field[i][j+1] == '#') and (field[i+1][j] == '#') and (field[i+1][j+1] == '.'):
        corner += 1      
print(corner)
