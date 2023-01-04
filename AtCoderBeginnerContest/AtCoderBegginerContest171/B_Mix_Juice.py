N, K = map(int, input().split(' '))
fruits = list(map(int, input().split(' ')))
fruits.sort()
 
print(sum(fruits[:K]))