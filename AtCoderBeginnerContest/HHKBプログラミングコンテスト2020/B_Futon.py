H, W = map(int, input().split(' '))
 
field = []
for i in range(H):
  field.append(list(input()))
#print(field)
 
check = []
cnt = 0
for i in range(H):
  next_check = []
  for j in range(W):
    if field[i][j] == '#':
      continue
    #ã
    if i - 1 >= 0 and field[i - 1][j] == '.':
      if ([[j, i - 1],[j, i]] not in check) and ([[j, i - 1],[j, i]] not in next_check):
        cnt += 1
        next_check.append([[j, i - 1],[j, i]])
    #‰E
    if j + 1 < W and field[i][j + 1] == '.':
      if ([[j, i], [j + 1, i]] not in check) and ([[j, i], [j + 1, i]] not in next_check):
        cnt += 1
        next_check.append([[j, i], [j + 1, i]])
    #‰º
    if i + 1 < H and field[i + 1][j] == '.':
      if ([[j, i], [j, i + 1]] not in check) and ([[j, i], [j, i + 1]] not in next_check):
        cnt += 1
        next_check.append([[j, i], [j, i + 1]])
    #¶
    if j - 1 >= 0 and field[i][j - 1] == '.':
      if ([[j - 1, i], [j, i]] not in check) and ([[j - 1, i], [j, i]] not in next_check):
        cnt += 1
        next_check.append([[j - 1, i], [j, i]])
  check = next_check
  #print(check)
print(cnt)