#python3‚Å‚ÍTLE‚Ì‚½‚ßPyPy3
N = int(input())
mikan = list(map(int, input().split(' ')))
 
max_apple = -1
for i in range(N):
  minimum = mikan[i]
  for j in range(i, N):
    if mikan[j] < minimum:
      minimum = mikan[j]    
    tmp = minimum * (j - i + 1)
    if tmp > max_apple:
      max_apple = tmp
print(max_apple)
