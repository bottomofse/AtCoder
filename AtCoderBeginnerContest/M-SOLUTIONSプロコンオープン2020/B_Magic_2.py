red, green, blue = map(int, input().split(' '))
K = int(input())
 
for i in range(K + 1):
  for j in range(K + 1):
    for k in range(K + 1):
      if i + j + k == K:
        next_red = red * (2 ** i)
        next_green = green * (2 ** j)
        next_blue = blue * (2 ** k)
        if next_blue > next_green and next_green > next_red:
          print('Yes')
          exit()
print('No')