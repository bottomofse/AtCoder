X, K, D = map(int, input().split(' '))
if abs(K * D) <= abs(X):
  print(abs(X) - abs(K * D))
  exit()
tmp = abs(X) // abs(D)
tmp2 = K - tmp
if tmp2 % 2 == 0:
  print(abs(abs(X) - abs(D) * tmp))
else:
  print(abs(abs(X) - abs(D) * tmp - D))