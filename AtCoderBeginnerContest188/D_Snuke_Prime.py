N, C = map(int, input().split(' '))
 
event = []
for i in range(N):
  a, b, c = map(int, input().split(' '))
  a -= 1 
  event.append([a, c])
  event.append([b, -c])
event.sort()
 
sum_fee = 0
daily_fee = 0
day = 0
for x, y in event:
  if x != day:
    sum_fee += min(C, daily_fee) * (x - day)
    day = x
  daily_fee += y
print(sum_fee)
