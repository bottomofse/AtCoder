N = int(input())
data_list = list(map(int, input().split(' ')))
 
result = 0
sum_data = 0
for i in range(N - 1):
  sum_data += data_list[i]
  result += sum_data * data_list[i + 1]
print(result % (10 ** 9 + 7))