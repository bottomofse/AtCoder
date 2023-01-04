N = int(input())
A = list(map(int, input().split(' ')))
cur_sum = sum(A)
Adic = {}
for i in A:
  Adic[i] = Adic[i] + 1 if i in Adic else 1
Q = int(input())
for i in range(Q):
  b, c = map(int, input().split(' '))
  if b not in Adic:
    print(cur_sum)
    continue
  tmp_cnt = Adic[b]
  cur_sum = cur_sum - tmp_cnt * b + tmp_cnt * c
  print(cur_sum)
  Adic[b] = 0
  Adic[c] = Adic[c] + tmp_cnt if c in Adic else tmp_cnt
