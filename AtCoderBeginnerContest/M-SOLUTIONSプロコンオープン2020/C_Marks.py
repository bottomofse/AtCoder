N, K = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
 
#�ŏ��̊y��̌v�Z
for i in range(K, N):
  if data[i] > data[i - K]:
    print('Yes')
  else:
    print('No')