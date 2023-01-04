N = int(input())
 
cnt = 0
for i in range(1, N + 1):
  str_10 = str(i)
  tmp = i
  str_8 = ''
  while tmp > 8:
    amari = tmp % 8
    str_8 = str(amari) + str_8
    tmp = int(tmp / 8)
  str_8 = str(tmp) + str_8
  if '7' not in str_10 and '7' not in str_8:
    cnt += 1
print(cnt)
