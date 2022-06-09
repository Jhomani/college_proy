from src.utils import my_round

# https://byjus.com/double-integral-calculator/

N = 1
y_top = 6
y_bottom = 4

def x_top(x = 1.0, rounded = True):
  res = 7

  return my_round(res,5) if rounded else res

def x_bottom(x = 1.0, rounded = True):
  res = 5

  return my_round(res,5) if rounded else res

def input_fun(x: float, y: float, rounded = True):
  res = (x + y)

  return my_round(res,5) if rounded else res

#  Calculation from here
hx = (y_top - y_bottom) / N

print(f'hx = {my_round(hx)}')
acumulated = 0

def get_coof(position: int):
  coefficient = 1

  if(position != 0 and position != N):
    coefficient = 2

  return coefficient

for i in range(N + 1):
  param_x = y_bottom + (hx*i)
  hy = (x_top(param_x) - x_bottom(param_x)) / N
  y_acumulated = 0

  print(f'  hy = {hy}')
  for j in range(N + 1):
    param_y = x_bottom(param_x) + (hy*j)

    res = input_fun(param_x,param_y) 
    y_acumulated += get_coof(j)*res

    print(f'  G({my_round(param_x)},{my_round(param_y)}) = {get_coof(j)}*{res}')

  res = my_round((hy/2)*y_acumulated)

  acumulated += get_coof(i)*res

  print(f'f(x{i}) = {get_coof(i)}*{res}')

final_res = (hx/2)*acumulated
print(f'I = {my_round(final_res)}')
