x, y, gx, gy = map(int, input().split(' '))
a = 0
 
a = (gy * x + gx * y) / (gy + y)
print(a)
