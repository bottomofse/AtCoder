X, Y = map(int, input().split(' '))
 
for i in range(X + 1):
  legs = 2 * i + 4 * (X - i)
  if legs == Y:
    print('Yes')
    exit()
print('No')