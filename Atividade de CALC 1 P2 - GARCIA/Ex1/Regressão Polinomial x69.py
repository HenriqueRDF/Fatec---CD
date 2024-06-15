import matplotlib.pyplot as plt
import math
import random

lista = [(x, x**69) for x in [random.uniform(-50, 50) for _ in range(10000)]]
def grad(a,b):
  grada = sum([-2*(lista[i][1] - a*lista[i][0]**69 - b)*(lista[i][0]**69) for i in range(len(lista))])
  gradb = sum([-2*(lista[i][1] - a*lista[i][0]**69 - b) for i in range(len(lista))])
  return [grada,gradb]

def dist(anterior,novo):
  zs = zip(anterior,novo)
  acc = 0
  for [p1,p2] in zs:
    acc += (p1-p2)**2

  return math.sqrt(acc)

def grad_desc(lr,xn,yn,tol):
  d = float('inf')
  k = 0
  while d > tol and k < 1000000:
    xn1 = xn - lr * grad(xn,yn)[0]
    yn1 = yn - lr * grad(xn,yn)[1]
    d = dist([xn,yn],[xn1,yn1])

    if any(abs(val) > 1e100 for val in [xn1, yn1, d]):
      print(f"Overflow {k}. PARA.")
      break
    
    xn = xn1
    yn = yn1
    k += 1
  return [xn1,yn1,k]

z = grad_desc(1e-18, 1, 0, 1e-18)
print(z)

x = [lista[i][0] for i in range(len(lista))]
y = [lista[i][1] for i in range(len(lista))]
a, b = z[0], z[1]
x1 = [int(i) for i in range(int(min(x)-1),int(max(x)+1))]
y1 = [a * xx**69 + b for xx in x1]

plt.figure(figsize=(11, 7))
plt.scatter(x,y)
plt.plot(x1,y1)
plt.show()