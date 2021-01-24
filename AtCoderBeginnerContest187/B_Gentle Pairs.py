N = int(input())
point_list = []
for i in range(N):
  point_list.append(list(map(int, input().split(' '))))
 
cnt = 0
for i in range(len(point_list) - 1):
  for j in range(i + 1, len(point_list)):
    x_diff = point_list[i][0] - point_list[j][0]
    y_diff = point_list[i][1] - point_list[j][1]
    #print([x_diff, y_diff])
    if (x_diff != 0) and (-1 <= (y_diff / x_diff) <= 1):
      cnt += 1
print(cnt)