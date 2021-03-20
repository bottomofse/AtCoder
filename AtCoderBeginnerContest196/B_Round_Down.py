data = input()
if '.' in data:
  print(data[:data.find('.')])
else:
  print(data)