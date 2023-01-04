N, X = map(int, input().split(' '))
res = X
score_list = list(input())
for i in score_list:
  if i == 'o':
    res += 1
  elif res > 0:
    res -= 1
  #print(res)
print(res)