N = int(input())
edge_list = list(map(int, input().split(' ')))
edge_list.sort()
cnt = 0
for i in range(N-2):
  for j in range(i + 1, N -1):
    for k in range(j + 1, N):
      #print([edge_list[i], edge_list[j], edge_list[k]])
      if (edge_list[i] != edge_list[j]) and \
      (edge_list[j] != edge_list[k]) and \
      (edge_list[i] + edge_list[j] > edge_list[k] ):
        cnt = cnt + 1
print(cnt)