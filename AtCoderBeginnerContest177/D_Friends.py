class UnionFind():  
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  
  def find(self, x):
    #print(x)
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
      x, y = y, x
    
    self.parents[x] += self.parents[y]
    self.parents[y] = x
    
  def size(self, x):
    return -self.parents[self.find(x)]

N, M = map(int, input().split(' '))
unionfind = UnionFind(N)
#print(unionfind.parents)

for i in range(M):
  X, Y = map(int, input().split(' '))
  X -= 1
  Y -= 1
  unionfind.union(X, Y)
  #print(unionfind.parents)

res = 0
for i in range(N):
  res = max(res, unionfind.size(i))
print(res)