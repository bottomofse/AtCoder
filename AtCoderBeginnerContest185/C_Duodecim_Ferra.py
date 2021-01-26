num = int(input()) - 1
numer = 1
for i in range(num,num - 11, -1):
  numer *= i
denor = 1
for i in range(11, 0, -1):
  denor *= i
print(numer // denor)