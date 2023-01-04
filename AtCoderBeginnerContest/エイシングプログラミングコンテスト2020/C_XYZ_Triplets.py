N = int(input())
 
answer = {}
for i in range(1, 105):
  for j in range(1, 105):
    for k in range(1, 105):
      result = i**2 + j**2 + k**2 + i * j + j * k + k * i
      if result in answer:
        answer[result] += 1
      else:
        answer[result] = 1
for i in range(1, N + 1):
  if i in answer:
    print(answer[i])
  else:
    print(0)