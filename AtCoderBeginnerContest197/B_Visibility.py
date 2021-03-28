H, W, X, Y = map(int,input().split(' '))
field = []
for i in range(H):
  field.append(list(input()))
X -= 1
Y -= 1
cnt = 1
#ã
for i in range(X - 1, -1, -1):
  if i >= 0 and field[i][Y] == '#':
    break
  if i >= 0 and field[i][Y] == '.':
    cnt += 1
#‰º
for i in range(X + 1, H):
  if i < H and field[i][Y] == '#':
    break
  if i < H and field[i][Y] == '.':
    cnt += 1
#¶
for i in range(Y - 1, -1, -1):
  if i >= 0 and field[X][i] == '#':
    break
  if i >= 0 and field[X][i] == '.':
    cnt += 1
#‰E
for i in range(Y + 1, W):
  if i < W and field[X][i] == '#':
    break
  if i < W and field[X][i] == '.':
    cnt += 1
print(cnt)