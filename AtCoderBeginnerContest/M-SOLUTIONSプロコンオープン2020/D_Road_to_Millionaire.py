N = int(input())
d = list(map(int, input().split(' ')))
money = 1000
kabuken = 0
for i in range(N - 1):
  if d[i + 1] > d[i]:
    kabuken += money // d[i]
    money %= d[i]
  elif d[i + 1] < d[i]:
    money += d[i] * kabuken
    kabuken = 0
money += d[-1] * kabuken
print(money)
