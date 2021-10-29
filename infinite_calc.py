while True:
  
  print()
  num_1 = input('Set first number: ')
  num_2 = input('Set another number: ')
  operador = input('Set operator: ')
  
  if not num_1.isnumeric() or not num_2.isnumeric():
    print('You need to type a number.')
    continue
  
  num_1 = int(num_1)
  num_2 = int(num_2)
  
  # + - * /
  if operador == '+':
    print(num_1 + num_2)
  elif operador == '-':
    print(num_1 - num_2)
  elif operador == '*':
    print(num_1 * num_2)
  elif operador == '/':
    print(num_1 / num_2)
  else:
    print('Not valid')
