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