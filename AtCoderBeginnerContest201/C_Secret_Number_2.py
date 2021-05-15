data = list(input())
cnt = 0
for i in range(10000):
  list_i = []
  if i < 1000:
    list_i = list(map(int,list(('000' + str(i))[-4:])))
  else:
    list_i = list(map(int, list(str(i))))
  correct = True
  for idx, value in enumerate(data):
    if value == 'o':
      if idx not in list_i:
        correct = False
        break
      continue
    if value == 'x':
      if idx in list_i:
        correct = False
        break
      continue
  if correct:
    cnt += 1
print(cnt)