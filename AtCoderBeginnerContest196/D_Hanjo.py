H, W, A, B = map(int, input().split(' '))
 
field = [[False for i in range(W)] for j in range(H)]
#print(field)
 
def search(x, y, tatami_rest):
  if y == H:
    if tatami_rest == 0:
      return 1
    else:
      return 0
  if x == W:
    return search(0, y + 1, tatami_rest)
  if field[y][x]:
    return search(x + 1, y, tatami_rest)
  
  ret = 0
  
  #c’u‚«
  if y + 1 < H and (not field[y + 1][x]) and tatami_rest > 0:
    field[y][x] = True
    field[y + 1][x] = True
    ret += search(x + 1, y, tatami_rest - 1)
    field[y][x] = False
    field[y + 1][x] = False
  
  #‰¡’u‚«
  if x + 1 < W and (not field[y][x + 1]) and tatami_rest > 0:
    field[y][x] = True
    field[y][x + 1] = True
    ret += search(x + 1, y, tatami_rest - 1)
    field[y][x] = False
    field[y][x + 1] = False
  
  #’u‚©‚È‚¢
  ret += search(x + 1, y, tatami_rest)
  
  return ret
 
print(search(0, 0, A))