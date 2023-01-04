H, W = map(int, input().split(' '))
 
min_block = 101
block_list = []
for i in range(H):
  tmp = list(map(int, input().split(' ')))
  tmp_min = min(tmp)
  if tmp_min < min_block:
    min_block = tmp_min
  block_list.append(tmp)
cnt = 0
for i in range(H):
  for j in range(W):
    cnt += (block_list[i][j] - min_block)
print(cnt)