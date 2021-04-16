S = input()
 
max_r = 0
cnt_r = 0
for i in range(len(S)):
  if S[i] == 'R':
    cnt_r += 1
  else:
    cnt_r = 0
  if cnt_r > max_r:
    max_r = cnt_r
print(max_r)