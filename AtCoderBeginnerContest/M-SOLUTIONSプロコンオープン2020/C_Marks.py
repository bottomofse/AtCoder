N, K = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
 
#Å‰‚ÌŠyŠí‚ÌŒvŽZ
for i in range(K, N):
  if data[i] > data[i - K]:
    print('Yes')
  else:
    print('No')