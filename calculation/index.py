from .utils import * 

# '-23x**2-2x-e**x+3'
# 'x**3-x-1'
# 'x**-2**-x'
# 'e**x+2**-x+2cosx-6'

def function(expesion: str, var:str = '1'):
  comp = ''
  f_num = ''

  result = 0
  t_fact = []

  p_res = None
  p_fact = []

  for char in expesion:
    if char == ' ':
      continue

    if isNum(char):
      f_num += char
    elif char == 'x':
      if p_res == None:
        t_fact.append(float(var))
      else:
        p_fact.append(float(var))
    elif char in ['+', '-']:
      if p_res != None:
        if f_num:
          p_fact.append(float(f_num))
        if p_fact:
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

      f_num = ''
      p_res = 0
    elif char == ',':
      if f_num:
        p_fact.append(float(f_num))
      p_res += applyFac(p_fact) 
      f_num = ''

      p_fact = [p_res]
      p_res = 0 
    elif char == ')':
      first_parm = None

      if comp in ['pow']:
        first_parm = p_fact.pop(0)

      if f_num:
        p_fact.append(float(f_num))
      p_res += applyFac(p_fact) 
      f_num = ''

      t_fact.append(calcFunction(comp, p_res, first_parm))

      p_fact = []
      p_res = None
      comp = ''
    else:
      comp += char

  if f_num:
    t_fact.append(float(f_num))
  result += applyFac(t_fact)
      
  return result