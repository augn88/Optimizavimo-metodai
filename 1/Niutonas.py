from sympy import symbols, N, lambdify
import matplotlib.pyplot as plt
import numpy as np


x = symbols('x')
a = 7
b = 6
f = ((x**2 - a)**2) / b - 1
epsilon = 10**-4
fFirstDerivative = (2*x*(x**2-7))/3
fSecondDerivative = (6*x**2-14)/3
x0 = 5
step = epsilon+1
iteration = 1
index = 0
xpoints = []
ypoints = []
print(f"x0 = {x0}. Pradedami skaiciavimai")

while step > epsilon:
    xpoints.append(x0)
    firstDer = fFirstDerivative.subs(x, x0) 
    secondDer = fSecondDerivative.subs(x, x0)
    step = fFirstDerivative.subs(x, x0) / fSecondDerivative.subs(x, x0)
    print(f"{iteration}:\tžingsnis = {N(step):.4f} vidurio taškas = {N(x0):.4f}")
    x0 = x0 - step
    
    iteration += 1

print(f"Galutinis vidurio taskas yra {N(x0):.4f}")

while len(xpoints) != len(ypoints):     
   ypoints.append(N(f.subs(x, xpoints[index])))
   index += 1
x_vals = [N(val) for val in xpoints]
y_vals = [N(val) for val in ypoints]
fnum = lambdify(x, f, 'numpy')
fxVals = np.linspace(0,5 ,100)
fyVals = fnum(fxVals)
plt.plot(fxVals, fyVals)
plt.plot(x_vals, y_vals, marker = "o", linestyle = "")

plt.show()