alphabet = 'abcdefghijklmnopqrstuvwxyz'
Base_26 = {}
for i in range(1, 27):
  Base_26[str(i)] = alphabet[i - 1]
a = int(input())
trans_26 = []
while True:
  amari = a % 26
  if amari == 0:
    amari = 26
  trans_26.insert(0, str(amari))
  a -= amari
  a = a // 26
  if a == 0:
    break
ans = ''
#print(trans_26)
for i in trans_26:
  ans += Base_26[str(i)]
print(ans)