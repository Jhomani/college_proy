from genericpath import commonprefix
import math
from src.utils import my_round

top = 2
bottom = 1
N = 6

def input_fun(x: float, rounded = True):
  res = (4 - (4/9)*x**2)**(1/2)

  if(rounded):
    res = my_round(res,5)

  return res 

h = (top - bottom) / N
acumulated = 0

print(f'h = {my_round(h, 5)}')

for i in range(N+1):
  pararm = bottom + (h*i)
  res = input_fun(pararm) 
  coefficient = 1

  if(i not in [0,N]):
    if(N == 2 and i == 1):
      coefficient = 4
    elif(N == 3 and i in [1,2]):
      coefficient = 3
    elif(N % 3 == 0 and i % 3 == 0):
      coefficient = 2
    elif(N % 3 == 0):
      coefficient = 3
    elif(N % 2 == 0 and i % 2 == 0):
      coefficient = 2
    elif(N % 2 == 0):
      coefficient = 4

  print(f'{coefficient}*f(x{i}) = ({coefficient})*{res}  ({my_round(pararm, 9)})')

  acumulated += coefficient * res

# last_coe = (3/8) if (N % 3 == 0) else (1/3)
last_coe = 1/3
final_res = (last_coe*h)*acumulated
print(f'I = {my_round(final_res, 5)} ({my_round(last_coe, 5)})')
