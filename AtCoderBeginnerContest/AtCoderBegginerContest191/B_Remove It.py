N, X = input().split(' ')
data = input().split(' ')
 
out = []
for i in data:
  if i != X:
    out.append(i)
print(' '.join(out))
