S = input()
for i in range(len(S)):
  if i % 2 == 1:
    #����
    if S[i] in 'abcdefghijklmnopqrstuvwxyz':
      print('No')
      exit()
  else:
    #�
    if S[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      print('No')
      exit()
print('Yes')