data = input()
int_data = int(data)
n = len(data) // 2 + 1
cnt = 0
for i in range(1, 10 ** n):
  tmp = str(i) * 2
  if int(tmp) <= int_data:
    cnt += 1
print(cnt)