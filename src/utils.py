from math import floor 

sub_nums = {
  0: '₀',
  1: '₁',
  2: '₂',
  3: '₃',
  4: '₄',
  5: '₅',
  6: '₆',
  7: '₇',
  8: '₈',
  9: '₉',
}
suber_nums = {
  0: '⁰',
  1: '¹',
  2: '²',
  3: '³',
  4: '⁴',
  5: '⁵',
  6: '⁶',
  7: '⁷',
  8: '⁸',
  9: '⁹',
}

def subs(num: int):
  resp = ''

  if num == 0:
    resp = sub_nums[0]

  while num > 0:
    last_num = num % 10
    resp = sub_nums[last_num] + resp
    num = floor(num/10)

  return resp

def middleNum(min, max, decs = 5):
  rang = max + min
  rounded = round(rang / 2, decs)

  return rounded

import math

def isNum(character: str):
  res = False;

  if character in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
    res = True

  return res

def applyFac(facts: list):
  total = 1

  for fact in facts:
    total *= fact

  return total

def calcFunction(fun: str, val: float, p_val = 1):
  res = 1

  if fun == 'cos':
    res = math.cos(val)
  elif fun == 'sin':
    res = math.sin(val)
  elif fun == 'tan':
    res = math.tan(val)
  elif fun == 'ln':
    res = math.log(val)
  elif fun == 'pow':
    res = math.pow(p_val, val)
  else:
    res = val
  
  return res