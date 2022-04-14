from ..utils import isNum, applyFac, calcFunction 
import math

def function(expesion: str, var:str = '1'):
  comp = ''
  f_num = ''

  result = 0
  t_fact = []

  p_res = None
  p_fact = []
  p_base = None

  for char in expesion:
    if char == ' ':
      continue

    if isNum(char):
      f_num += char
    elif char == 'e':
      if p_res == None:
        t_fact.append(math.e)
      else:
        p_fact.append(math.e)
    elif char == 'x':
      if p_res == None:
        t_fact.append(float(var))
      else:
        p_fact.append(float(var))
    elif char in ['+', '-']:
      if p_res != None:
        if f_num:
          p_fact.append(float(f_num))
        if p_fact and p_base != None:
          p_base += applyFac(p_fact) 
        if p_fact and comp != 'pow':
          p_res += applyFac(p_fact) 

        p_fact = [1] if char == '+' else [-1]
      else:
        if f_num:
          t_fact.append(float(f_num))
        if t_fact:
          result += applyFac(t_fact)

        t_fact = [1] if char == '+' else [-1]

      f_num = ''
    elif char == '(':
      if f_num:
        t_fact.append(float(f_num))

      if comp == 'pow':
        p_base = 0

      f_num = ''
      p_res = 0
    elif char == ',':
      if f_num:
        p_fact.append(float(f_num))
      p_base += applyFac(p_fact) 
      f_num = ''

      p_fact = []
    elif char == ')':
      if f_num:
        p_fact.append(float(f_num))
      p_res += applyFac(p_fact) 
      f_num = ''

      t_fact.append(calcFunction(comp, p_res, p_base))

      p_fact = []
      p_base = None
      p_res = None
      comp = ''
    else:
      comp += char

  if f_num:
    t_fact.append(float(f_num))
  result += applyFac(t_fact)
      
  return result