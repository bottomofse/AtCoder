X, Y, A, B = map(int, input().split(' '))
cnt = 0
while A * X <= X + B and A * X < Y:
  X *= A
  cnt += 1
print(cnt + (Y - X - 1) // B)
