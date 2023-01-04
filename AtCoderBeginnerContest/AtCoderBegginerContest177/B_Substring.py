S = input()
T = input()
res_min = 10000
for i in range(len(S) - len(T) + 1):
  cnt = 0
  for j in range(len(T)):
    if S[i + j] != T[j]:
      cnt += 1
  if res_min > cnt:
    res_min = cnt
print(res_min)