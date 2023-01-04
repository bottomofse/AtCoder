N = int(input())
first = 0
first_name = ''
second = 0
second_name = ''
for i in range(N):
  S, T = input().split(' ')
  T = int(T)
  if T > first:
    second = first
    second_name = first_name
    first = T
    first_name = S
  elif T > second:
    second = T
    second_name = S
print(second_name)