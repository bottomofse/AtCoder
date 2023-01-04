N, M, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
 
Ruiseki_A = [0]
for i in range(N):
  last = Ruiseki_A[-1]
  Ruiseki_A.append(last + A[i])
Ruiseki_B = [0]
for i in range(M):
  last = Ruiseki_B[-1]
  Ruiseki_B.append(last + B[i])
 
def SearchIdx(ArgK, Hairetsu):
  left = 0
  right = len(Hairetsu) - 1
  while right - left > 1:
    mid = (left + right) // 2
    if Hairetsu[mid] > ArgK:
      right = mid
      continue
    if Hairetsu[mid] <= ArgK:
      left = mid
      continue
  if Hairetsu[left] <= ArgK and Hairetsu[right] > ArgK:
    return left
  if Hairetsu[left] <= ArgK and Hairetsu[right] <= ArgK:
    return right
  return left
 
max_book_cnt = 0
for i in range(N + 1):
  book_cnt = 0
  if K - Ruiseki_A[i] >= 0:
    rest_read_time = K - Ruiseki_A[i]
    book_cnt = i
  else:
    rest_read_time = K
    book_cnt = 0
  book_cnt += SearchIdx(rest_read_time, Ruiseki_B)
  if book_cnt > max_book_cnt:
    max_book_cnt = book_cnt
print(max_book_cnt)