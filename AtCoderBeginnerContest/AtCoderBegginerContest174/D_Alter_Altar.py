N = int(input())
stones = list(input())
top = 0
bottom = N - 1
cnt = 0
while top < bottom:
  while top < N and stones[top] != 'W':
    top += 1
  while bottom > -1 and stones[bottom] != 'R':
    bottom -= 1
  if top >= bottom:
    break
  stones[top], stones[bottom] = stones[bottom], stones[top]
  cnt += 1
print(cnt)
