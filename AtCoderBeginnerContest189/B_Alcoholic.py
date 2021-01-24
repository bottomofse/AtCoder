#N”t@ƒAƒ‹ƒR[ƒ‹‚ÌŒÀŠEX
N, X = map(int, input().split(' '))
 
alc_max = 100 * X
alc_now = 0
alc_cup = 0
output = -1
for i in range(N):
  V, X = map(int, input().split(' '))
  alc_now = alc_now + V * X
  alc_cup = alc_cup + 1
  if alc_now > alc_max:
    output = alc_cup
    break
print(output)
