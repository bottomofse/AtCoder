N = int(input())
S = list(input())
S_zenhan = S[:N]
S_kouhan = S[-N:]
Q = int(input())
flg = True
for i in range(Q):
  T, A, B = map(int, input().split(' '))
  if T == 1:
    if flg:
      if B <= N:
        tmp = S_zenhan[A - 1]
        S_zenhan[A - 1] = S_zenhan[B - 1]
        S_zenhan[B - 1] = tmp
      elif A > N:
        tmp = S_kouhan[A - 1 - N]
        S_kouhan[A - 1 - N] = S_kouhan[B - 1 -N]
        S_kouhan[B - 1 - N] = tmp
      else:
        tmp = S_zenhan[A - 1]
        S_zenhan[A - 1] = S_kouhan[B - 1 - N]
        S_kouhan[B - 1 - N] = tmp
    else:
      if B <= N:
        tmp = S_kouhan[A - 1]
        S_kouhan[A - 1] = S_kouhan[B - 1]
        S_kouhan[B - 1] = tmp
      elif A > N:
        tmp = S_zenhan[A - 1 - N]
        S_zenhan[A - 1 - N] = S_zenhan[B - 1 -N]
        S_zenhan[B - 1 - N] = tmp
      else:
        tmp = S_kouhan[A - 1]
        S_kouhan[A - 1] = S_zenhan[B - 1 - N]
        S_zenhan[B - 1 - N] = tmp
  else:
    flg = not flg
if flg:
  print(''.join(S_zenhan) + ''.join(S_kouhan))
else:
  print(''.join(S_kouhan) + ''.join(S_zenhan))