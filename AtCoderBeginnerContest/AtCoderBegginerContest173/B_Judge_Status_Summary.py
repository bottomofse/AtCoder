AC = 0
WA = 0
TLE = 0
RE = 0

N = int(input())
for i in range(N):
  tmp = input()
  if tmp == 'AC':
    AC += 1
    continue
  if tmp == 'WA':
    WA += 1
    continue
  if tmp == 'TLE':
    TLE += 1
    continue
  if tmp == 'RE':
    RE += 1
    continue
print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))
