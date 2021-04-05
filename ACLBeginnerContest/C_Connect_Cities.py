N, M = map(int, input().split(' '))
 
parent = {}
rank = {}
 
#‰Šú‰»
for i in range(N):
  parent[i + 1] = i + 1
  rank[i + 1] = 0
 
def find(par, target):
  if par[target] == target:
    return target
  else:
    a = find(par, par[target])
    return a
 
def isSame(par, a, b):
  return find(par, a) == find(par, b)
 
def unite(par, x, y):
  x = find(par, x)
  y = find(par, y)
  if x == y:
    return
  if rank[x] < rank[y]:
    par[x] = y
  else:
    par[y] = x
    if rank[x] == rank[y]:
      rank[x] += 1
 
#“¹˜HÚ‘±
for i in range(M):
  a, b = map(int, input().split(' '))
  if parent[a] != parent[b]:
    unite(parent, a, b)
cnt_dic = {}
for i in parent:
  cnt_dic[find(parent, parent[i])] = 0
print(len(cnt_dic) - 1)