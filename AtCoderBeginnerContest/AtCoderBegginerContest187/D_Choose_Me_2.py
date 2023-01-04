N = int(input())

sum_aoki = 0
voter_list = []
for i in range(N):
  A, B = map(int, input().split(' '))
  sum_aoki += A
  voter_list.append(2 * A + B)
voter_list.sort(reverse=True)
#print(voter_list)
#print(sum_aoki)

cnt = 1
for i in voter_list:
  sum_aoki -= i
  if sum_aoki >= 0:
    cnt += 1
  else:
    break
print(cnt)