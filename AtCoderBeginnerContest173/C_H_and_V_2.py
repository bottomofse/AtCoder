H, W, K = map(int, input().split(' '))
field = [list(input()) for i in range(H)]
res = 0
for i in range(1<<H):
  for j in range(1<<W):
    cnt = 0
    for m in range(H):
      for n in range(W):
        if i>>m & 1: continue 
        if j>>n & 1: continue
        if field[m][n] == '#': cnt += 1
    res = res + 1 if cnt == K else res
print(res)
