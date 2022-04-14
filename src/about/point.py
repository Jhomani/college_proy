from ..calculation.fun import function
from ..utils import middleNum, subs

def point():
  fung = input("Function g: ")
  err = input("Enter the error: ")
  interv = input("Enter the interval: ")

  interv = interv.split(',')
  interv = [float(num) for num in interv] 
  err = float(err)

  results = [False, False]

  decm = 7

  print('')
  for i, num in enumerate(interv):
    result = round(function(fung, num), decm) 
    results[i] = result >= interv[0] and result <= interv[1]

    print(f'g({num}) = {result}')

  if(results[0] and results[1]):
    print('Cumple')

  x0 = middleNum(interv[0], interv[1], decm)
  n = 1
  calc_err = 10000

  print('')
  while calc_err > err:
    current = round(function(fung, x0), decm)
    if n > 1:
      calc_err = round(abs(x0 - current), 8)

    print(f'n = {n}  x{subs(n)} = g(x{subs(n-1)}) = {current}    err = {calc_err}')

    x0 = current
    n +=1

  print('')
  print(f'|x{subs(n-2)}-x{subs(n-1)}| = {calc_err} < {err}')
  print(f'Sol: x{subs(n-1)} = {x0}')
