data = input()
correct = data.count('o')
question = data.count('?')
 
if correct > 4:
  print(0)
  exit()
if correct == 4:
  print(24)
  exit()
if correct == 3:
  if question == 0:
    print(36)
  else:
    print(24 * question + 36)
  exit()
if correct == 2:
  if question == 0:
    print(14)
  else:
    print(6 * 2 * (question ** 2) + 4 * 6 * question + 14)
  exit()
if correct == 1:
  if question == 0:
    print(1 ** 4)
  else:
    print(4 * (question ** 3) + 6 * (question ** 2) + 4 * (question ** 1) + 1)
  exit()
if correct == 0:
  if question == 0:
    print(0)
  else:
    print(question ** 4)
  exit()