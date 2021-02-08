import itertools
 
input_str = input()
input_array = [int(i) for i in list(input_str)]
 
for i in range(len(input_array), 0, -1):
  for j in itertools.combinations(input_array, i):
    if sum(j) % 3 == 0:
      print(len(input_array) - i)
      exit()
print(-1)
