N = int(input())

S_list = []
for i in range(N):
  S_list.append(input())
#print(S_list)
cnt = 1
for i in range(len(S_list) - 1, -1, -1):
  if S_list[i] == 'OR':
    cnt += 2 ** (i + 1)
print(cnt)