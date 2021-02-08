N = int(input())
data = [int(i) for i in list(input().split(' '))]
 
max_xloc = -100000000
cur_xloc = 0
before_sum = 0
max_plus = 0
for i in data:
  before_sum += i
  if before_sum > max_plus:
    max_plus = before_sum
  if cur_xloc + max_plus > max_xloc:
    max_xloc = cur_xloc + max_plus
  cur_xloc += before_sum
print(max_xloc)
