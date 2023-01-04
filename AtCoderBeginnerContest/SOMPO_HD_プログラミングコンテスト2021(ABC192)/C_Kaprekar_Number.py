N, K = map(int, input().split(' '))
 
def g_x1(number):
  tmp = sorted(list(str(number)), reverse=True)
  ret = int(''.join(tmp))
  return ret
 
def g_x2(number):
  tmp = sorted(list(str(number)))
  ret = int(''.join(tmp))
  return ret
 
cur = N
for i in range(K):
  cur = g_x1(cur) - g_x2(cur)
print(cur)