from src.utils import my_round, subs

top = 3
bottom = 0
h = 1
out = 1

# Calculation
def input_fun(x: float, y: float, rounded = True):
  res = x + y

  return my_round(res,5) if rounded else res

N = round((top - bottom) / h)
print(f'N = {N}\n')

xk = bottom
yk = out

for i in range(N):
  print(f'k = {i}')
  res = my_round(yk + h*input_fun(xk, yk))
  print(f'  y{subs(i+1)} =  {yk} + {h}*({input_fun(xk, yk)}) = {res}')
  yk = res
  xk = my_round(xk + h)

print('\n_______________ modified ________________\n')

xk = bottom
yk = out

for i in range(N):
  print(f'k = {i}')
  partial_res = my_round(yk + h*input_fun(xk, yk))
  plus_x = my_round(xk + h)

  res = my_round(yk + (h/2)*(input_fun(xk, yk) + input_fun(plus_x, partial_res)))

  print(f'  y{subs(i+1)} = {yk} + ({h}/2)*(f({xk},{yk}) + f({plus_x}, {partial_res})) = {res}')
  print(f'    f({xk},{yk}) = {input_fun(xk, yk)}')
  print(f'    f({plus_x}, {partial_res}) = {input_fun(plus_x, partial_res)}')
  
  yk = res
  xk = my_round(xk + h)
