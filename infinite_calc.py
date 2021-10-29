while True:
  print()
  num1 = input('Set first number: ')
  num2 = input('Set another number: ')
  operator = input('Digit an operator ')

  if not num1.isnumeric() or not num2.isnumeric():
    print("You need to put a number here :)")
    continue

  if operator == '+':
    print(num1 + num2)
  elif operator == '-':
    print(num1 - num2)
  elif operator == '*':
    print(num1 * num2)
  else:
    print('Invalid Operation')