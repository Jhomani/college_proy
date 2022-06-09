from src.utils import my_round 

a = [
 [9,3,1,2], 
 [1,12,1,5], 
 [1,1,15,4], 
]
# a = [
#   [15, 3, 6],
#   [1, 12, 2]
# ]

target_er = 0.005; 

x1k = 0
x2k = 0
x3k = 0

k=1
er = 100

if(len(a) == 2):
  while(er > target_er):
    xk1 = my_round((1/a[0][0])*(a[0][2] - a[0][1]*x2k), 5)
    xk2 = my_round((1/a[1][1])*(a[1][2] - a[1][0]*xk1), 5)

    raw_numer = [xk1 - x1k,xk2 - x2k]
    numer = [my_round(z, 5) for z in raw_numer]
    den = [xk1,xk2]

    er = my_round(max([abs(z) for z in numer])/max([abs(z) for z in den]), 5);  
    print(f'(1/{a[0][0]})*({a[0][2]} - {a[0][1]}*{x2k}) = {xk1}')
    print(f'(1/{a[1][1]})*({a[1][2]} - {a[1][0]}*{xk1}) = {xk2}')
    print(f'error = {er} k = {k}')

    x1k, x2k = xk1, xk2
    k += 1

  print(f'\nSolution: {numer} / {den} = {er} < {target_er}')

if(len(a) == 3):
  while(er > target_er):
    xk1 = my_round((1/a[0][0])*(a[0][3] - a[0][1]*x2k - a[0][2]*x3k), 5)
    xk2 = my_round((1/a[1][1])*(a[1][3] - a[1][0]*xk1 - a[1][2]*x3k), 5)
    xk3 = my_round((1/a[2][2])*(a[2][3] - a[2][0]*xk1 - a[2][1]*xk2), 5)

    raw_numer = [xk1 - x1k,xk2 - x2k, xk3 - x3k]
    numer = [my_round(z, 5) for z in raw_numer]
    den = [xk1,xk2,xk3]
    er = my_round(max([abs(z) for z in numer])/max([abs(z) for z in den]), 5);  
    print(f'(1/{a[0][0]})*({a[0][3]} - ({a[0][1]}*{x2k}) - ({a[0][2]}*{x3k})) = {xk1}')
    print(f'(1/{a[1][1]})*({a[1][3]} - ({a[1][0]}*{xk1}) - ({a[1][2]}*{x3k})) = {xk2}')
    print(f'(1/{a[2][2]})*({a[2][3]} - ({a[2][0]}*{xk1}) - ({a[2][1]}*{xk2})) = {xk3}')
    print(f'error = {er} k = {k}')

    x1k, x2k, x3k = xk1, xk2, xk3
    k += 1

  print(f'\nSolution: {numer} / {den} = {er} < {target_er}')