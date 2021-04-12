import math
from decimal import Decimal
R, X, Y = input().split(' ')
distance = str((Decimal(X) ** Decimal('2')  + Decimal(Y) ** Decimal('2')) ** Decimal('0.5'))
if Decimal(distance) < Decimal(R):
  print(2)
else:
  print(math.ceil(Decimal(distance) / Decimal(R)))