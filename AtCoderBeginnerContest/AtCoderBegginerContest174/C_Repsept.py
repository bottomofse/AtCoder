K = int(input())
 
cur = 7
cnt = 1
exist = True
for i in range(K + 1):
  amari = cur % K
  if amari == 0:
    print(cnt)
    exit()
  cur = amari * 10 + 7
  cnt += 1
print(-1)