N, K = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
 
#最初の楽器の計算
for i in range(K, N):
  if data[i] > data[i - K]:
    print('Yes')
  else:
    print('No')