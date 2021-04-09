X, Y, A, B = map(int, input().split(' '))
cnt = 0
while True:
  if X + B > X * A and X * A < Y:
    X = X * A
    cnt += 1
  else:
    break  
print(cnt + ((Y - X -1) // B))
