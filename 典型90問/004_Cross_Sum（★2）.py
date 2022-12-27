H, W = map(int, input().split(' '))
row_sum = []
col_sum = [0 for i in range(W)]
data = []
for i in range(H):
  tmp = list(map(int, input().split(' ')))
  data.append(tmp)
  row_sum.append(sum(tmp))
for i in range(W):
  for j in range(H):
    col_sum[i] += data[j][i]
res = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
  for j in range(W):
    res[i][j] = str(row_sum[i] + col_sum[j] - data[i][j])
for i in res:
  print(' '.join(i))
