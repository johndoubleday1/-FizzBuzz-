def FizzBuzz (x):

  if ((x % 3.0== 0) and (x % 5.0== 0)) :
    return (print('FizzBuzz'))
  elif (x % 3.0== 0):
    return (print('Fizz'))
  elif (x % 5.0== 0):
    return (print('Buzz'))
  else:
    return (print('Nothing'))

while True:
  while True:
    try:
      x = (input('Give me a number:'))
      x = float(x)
      break
    except ValueError:
      print('Invalid input, try again:')
  FizzBuzz (x)
  while True:
    answer = input('Run again?(y/n):')
    if answer in ('y', 'n'):
      break
    print ('Invalid input.')
  if answer =='y':
    continue
  else:
    print ('Goodbye')
    break
 
