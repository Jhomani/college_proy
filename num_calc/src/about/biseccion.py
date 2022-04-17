from math import ceil, log
from ..calculation.fun import function
from ..utils import middleNum, subs

decs= 7

def biseccionMethod(a, b, n: int, err: float, func: str):
  print('', 'n = ln[(a -b) / E] / ln(2)', f'n = {n}', sep='\n')

  x =  b
  fa = -1
  fx = 1 

  ap_x = 0

  row_f = '|{:>3}|' + ('{:>10}|' * 6) + '{:^18}|'
  row = ['n', 'aᵢ', 'xᵢ', 'bᵢ', 'f(a)', 'f(x)', 'f(b)', '|x₂ - x₁| < E']

  print('-'*90, row_f.format(*row),'-'*90, sep='\n')

  for i in range(1, n+1):
    if (fa >= 0 and fx < 0) or (fa < 0 and fx >= 0):
      b = x
    elif (fx >= 0 and fb < 0) or (fx < 0 and fb >= 0):
      a = x

    x = middleNum(a, b, decs)

    fa = round(function(func, a), decs) 
    fx = round(function(func, x), decs) 
    fb = round(function(func, b), decs) 

    if i == n-1:
      ap_x = x

    if i == n:
      row = [i, a, x, b, '', '', '', '|x₂ - x₁| < E']
    else:
      row = [i, a, x, b, fa, fx, fb, '|x₂ - x₁| > E']

    print(row_f.format(*row))

  result = f'{round(abs(x-ap_x), decs)} < {err}'
  summary = f'|x{subs(n)} - x{subs(n-1)}| = |{x} - {ap_x}| = {result}'
  print('-'*90, summary, f'Sol: x{subs(n)} = {x}', sep='\n')


def master():
  func=input("Enter the function: ")
  err=input("Enter the error: ")
  interval=input("Enter the interval: ")

  interval = interval.split(',')
  err = float(err)
  interval = [float(num) for num in interval]

  lnArg = (interval[1] - interval[0]) / err
  n = ceil(log(lnArg) / log(2))

  biseccionMethod(interval[0], interval[1], n, err, func)