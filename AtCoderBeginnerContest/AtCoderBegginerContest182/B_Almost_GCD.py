N = int(input())
data = list(map(int, input().split(' ')))
 
K = 0
max_gcd = 0
for i in range(2, max(data) + 1):
  gcd = 0
  for j in data:
    if j % i == 0:
      gcd += 1
  if gcd >= max_gcd:
    max_gcd = gcd
    K = i
print(K)
