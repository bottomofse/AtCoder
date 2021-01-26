N, M, T = map(int, input().split(' '))
cur_battery = N
cur_t = 0
for i in range(M):
  A, B = map(int, input().split(' '))
  cur_battery -= A - cur_t
  if cur_battery <= 0:
    print('No')
    exit()
  #print(cur_battery)
  cur_battery += B - A
  if cur_battery > N:
    cur_battery = N
  #print(cur_battery)
  cur_t = B
rest = T - cur_t
if rest < cur_battery:
  print('Yes')
else:
  print('No')
