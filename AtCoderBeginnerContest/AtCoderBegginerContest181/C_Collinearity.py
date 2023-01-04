N = int(input())
 
#“_x,y
input_data = []
for i in range(N):
  x, y = map(int, input().split(' '))
  input_data.append([x, y])
 
#print(input_data)
for i in range(N - 2):
  for j in range(i + 1, N - 1):
    for k in range(j + 1, N):
      ax, ay = input_data[i]
      bx, by = input_data[j]
      cx, cy = input_data[k]
      ax -= cx
      ay -= cy
      bx -= cx
      by -= cy
      if ax * by == bx * ay:
        print('Yes')
        exit()
print('No')
