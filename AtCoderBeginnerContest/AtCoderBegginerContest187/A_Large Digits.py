A, B = input().split(' ')
SA = sum(list(map(int, list(A))))
SB = sum(list(map(int, list(B))))
if SA >= SB:
  print(SA)
else:
  print(SB)