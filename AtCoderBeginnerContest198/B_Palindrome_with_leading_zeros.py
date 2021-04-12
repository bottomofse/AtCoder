S = input()
for i in range(20):
  if S == S[::-1]:
    print('Yes')
    exit()
  S = '0' + S
print('No')