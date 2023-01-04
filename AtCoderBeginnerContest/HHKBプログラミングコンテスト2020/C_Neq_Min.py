N = int(input())
 
data = [1 for i in range(200001)]
input_data = list(map(int, input().split(' ')))
 
before = 0
for i in input_data:
  data[i] = 0
  for j in range(before, len(data)):
    if data[j] == 1:
      before = j
      print(j)
      break