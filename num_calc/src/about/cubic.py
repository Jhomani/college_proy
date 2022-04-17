from ..calculation.fun import function
from ..utils import subs

def master_cub():
  axisX = input("Enter axis X: ")
  axisY = input("Enter axis Y: ")
  params = input("Enter params: ")

  axisX = axisX.split(',')
  axisY = axisY.split(',')
  params = params.split(',')

  for i in range(len(axisX)):
    axisX[i] = float(axisX[i])
    axisY[i] = float(axisY[i])

  h=[0,0]
  a=[0,0,0]
  c=[0,0,0]
  b=[0,0]
  d=[0,0]

  # -------- 1 ---------
  print('', '1ᵒ hᵢ = x₍ᵢ₊₁₎ - xᵢ     where i = 0,1', sep='\n')
  for i in range(2):
    h[i] = round(axisX[i+1] - axisX[i], 5) 
    print(f'   h{subs(i)} = x{subs(i+1)} - x{subs(i)} = {h[i]}')

  # -------- 2 ---------
  print('', '2ᵒ aᵢ = f(xᵢ)     where i = 0,1,2', sep='\n')
  for i in range(3):
    a[i] = axisY[i]
    print(f'   a{subs(i)} = f(x{subs(i)}) = {a[i]}')

  # -------- 3 ---------
  print('', '3ᵒ calcular cᵢ', sep='\n')
  rows = {
    0: [1, 0, 0, 'c₀', 0],
    1: ['h₀', '2(h₀+h₁)', 'h₁', 'c₁', '3(a₂-a₁)/h₁ - 3(a₁-a₀)/h₀'],
    2: [0, 0, 1, 'c₃', 0],
  }

  row_f = '|{:^3} {:^8} {:^3}| |{:^4}|   |{:^28}|'
  for i in range(3):
    print('   ' + row_f.format(*rows[i]))

  print('')
  row_f = '|{:^3} {:^6} {:^3}| |{:^6}|   |{:^6}|'
  lef=0
  cen=0
  results = ''
  for i in range(3):
    if i == 1:
      cen = round(2*(h[0]+h[1]), 5)
      lef = round((3/h[1])*(a[2]-a[1]) - (3/h[0])*(a[1]-a[0]), 5)
      rows[i] = [h[0], cen, h[1], 'c₁', lef]
      c[i] = round(lef/cen,5)
    results += f'c{subs(i)} = {c[i]}  '
    print('   ' + row_f.format(*rows[i]))
  print('', f'   {cen}c₁ = {lef}   =>   {results}', sep='\n')

  # -------- 4 ---------
  print('', '4ᵒ bᵢ = 1/hᵢ (aᵢ₊₁ - aᵢ) - hᵢ/3 (2cᵢ + cᵢ₊₁)       where i = 0,1', sep='\n')
  for i in range(2):
    b[i] = round((1/h[i])*(a[i+1] - a[i]) - (h[i]/3)*(2*c[i]+c[i+1]), 5) 
    print(f'   b{subs(i)} = 1/{h[i]} ({a[i+1]} - {a[i]}) - {h[i]}/3 (2*{c[i]} + {c[i+1]}) = {b[i]}')

  # -------- 5 ---------
  print('', '5ᵒ dᵢ = (c₍ᵢ₊₁₎ - cᵢ)/3hᵢ     where i = 0,1', sep='\n')
  for i in range(2):
    d[i] = round((c[i+1]-c[i])/(3*h[i]), 5) 
    print(f'   d{subs(i)} = ({c[i+1]} - {c[i]})/3*{h[i]} = {d[i]}')

  # -------- Final ---------
  print('', 'Por tanto', 'sᵢ(x) = aᵢ + bᵢ(x-xᵢ) + cᵢ(x-xᵢ)² + dᵢ(x-xᵢ)³      where i = 0,1', sep='\n')

  funs = ['', '']
  funsDer = ['', '']

  for i in range(2):
    bs = f'+ {b[i]}' if b[i] >= 0 else f'- {abs(b[i])}'
    xs = f'-{axisX[i]}' if axisX[i] >= 0 else f'+{abs(axisX[i])}'
    cs = f'+ {c[i]}' if c[i] >= 0 else f'- {abs(c[i])}'
    ds = f'+ {d[i]}' if d[i] >= 0 else f'- {abs(d[i])}'

    aux = round(c[i]*2, 5)
    csd = f'+ {aux}' if c[i] >= 0 else f'- {abs(aux)}'
    aux = round(d[i]*3, 5)
    dsd = f'+ {aux}' if d[i] >= 0 else f'- {abs(aux)}'

    funs[i] = f'{a[i]} {bs}(x{xs}) {cs}pow(x{xs}, 2) {ds}pow(x{xs}, 3)' 
    funsDer[i] = f'{bs} {csd}(x{xs}) {dsd}pow(x{xs}, 2)' 
    print(f'   s{subs(i)}(x) = {a[i]} {bs}(x{xs}) {cs}(x{xs})² {ds}(x{xs})³', sep='\n')
    print(f"   s'{subs(i)}(x) = {bs} {csd}(x{xs}) {dsd}(x{xs}, 2)²")

  for num in params:
    print('', f'Testing with: {num}', sep='\n')
    for i in range(2):
      print(f"   s{subs(i)}({num}) = {round(function(funs[i], num), 5)}")
      print(f"   s'{subs(i)}({num}) = {round(function(funsDer[i], num), 5)}")
