import collections
import itertools
 
str_list = list(input())
 
if len(str_list) <= 2:
  for comb in itertools.permutations(str_list, len(str_list)):
    if int(''.join(comb)) % 8 == 0:
      print('Yes')
      exit()
  print('No')
  exit()
 
cnt = collections.Counter(str_list)
for i in range(112, 1000, 8):
  if not collections.Counter(str(i)) - cnt:
    print('Yes')
    exit()
print('No')
