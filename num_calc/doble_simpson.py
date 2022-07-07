import math
#from src.utils import my_round

def my_round(num: float | int, decimals = 5):
  aux_num = 1
  num_decimals = decimals

  while(num_decimals != 0):
    aux_num *= 10
    num_decimals -=1

  num = num * aux_num
  modul = (abs(num) % 1) * 10

  if(modul >= 5):
    num = ceil(num) if num > 0 else floor(num)
  else:
    num = floor(num) if num > 0 else ceil(num)

  return round(num/aux_num, decimals)

N = 150
y_top = math.sqrt(3)
y_bottom = 1

def x_top(x: float, rounded = True):
  res = x

  return my_round(res,5) if rounded else res

def x_bottom(x: float, rounded = True):
  res = 0

  return my_round(res,5) if rounded else res

def input_fun(x: float, y: float, rounded = True):
  res = x/(x**2+y**2)

  return my_round(res,5) if rounded else res

#  Calculation from here
hx = (y_top - y_bottom) / N

# print(f'hx = {my_round(hx)}')
acumulated = 0

def get_coof(position: int):
  coefficient = 1

  if(position not in [0,N]):
    if(N == 2 and position == 1):
      coefficient = 4
    elif(N == 3 and position in [1,2]):
      coefficient = 3
    elif(N % 3 == 0 and position % 3 == 0):
      coefficient = 2
    elif(N % 3 == 0):
      coefficient = 3
    elif(N % 2 == 0 and position % 2 == 0):
      coefficient = 2
    elif(N % 2 == 0):
      coefficient = 4

  return coefficient

for i in range(N + 1):
  param_x = y_bottom + (hx*i)
  hy = (x_top(param_x) - x_bottom(param_x)) / N
  y_acumulated = 0

  # print(f'  hy = {hy}')
  for j in range(N + 1):
    param_y = x_bottom(param_x) + (hy*j)

    res = input_fun(param_x,param_y) 
    y_acumulated += get_coof(j)*res

    # print(f'  G({my_round(param_x)},{my_round(param_y)}) = {res}*({get_coof(j)})')

  last_coe = (3/8) if (N % 3 == 0) else (1/3)
  partial_res = my_round((last_coe*hy)*y_acumulated)
  acumulated += get_coof(i)*partial_res

  # print(f'f(x{i}) = {partial_res}*({get_coof(i)})')

last_coe = (3/8) if (N % 3 == 0) else (1/3)
final_res = (last_coe*hx)*acumulated
print(f'I = {my_round(final_res)}')
