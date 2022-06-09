from src.utils import my_round

top = 4
bottom = 2
N = 7

def input_fun(x: float, rounded = True):
  res = x*(x+1)**(1/2)

  if(rounded):
    res = my_round(res,5)

  return res 

h = (top - bottom) / N
acumulated = 0

print(f'h = {my_round(h, 5)}')

for i in range(N +1):
  pararm = bottom + (h*i)
  res = input_fun(pararm) 
  coefficient = 1

  if(i != 0 and i != N):
    coefficient = 2

  acumulated += coefficient*res

  print(f'{coefficient}*f(x{i}) = {coefficient}*{res}  ({my_round(pararm, 9)})')


final_res = (h/2)*acumulated
print(f'I = {my_round(final_res, 5)}')
