from sympy import symbols, N, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
a = 7
b = 6
f =((x**2 - a)**2) / b - 1

epsilon = 10**-4
right = 10
left = 0
gr = 0.618
index = 0
iteration = 0
L = right - left
x1 = right - gr*L
x2 = left + gr*L
fx1 = f.subs(x, x1)
fx2 = f.subs(x, x2)
xpoints = []
ypoints = []

while L > epsilon:
    if f.subs(x,x2) < f.subs(x,x1):
        left = x1
        L = right - left
        x1 = x2
        x2 = left + gr*L
        fx2 = f.subs(x, x2)
        print("Keičiam kairę")
    else:
        right = x2
        L = right - left
        x2 = x1
        x1 = right - gr*L
        fx1 = f.subs(x, x1)
        print("Keičiam dešinę")
    iteration += 1
    center = N((left+right)/2)
    xpoints.append(center)
    print(f"{iteration}:\t K={N(left):.4f} vidurio taškas = {N(center):.4f} D={N(right):.4f}")
    
print(f"Galutinis vidurio taškas yra {N(center):.4f}")

while len(xpoints) != len(ypoints):     
   ypoints.append(f.subs(x, xpoints[index]))
   index += 1
x_vals = [N(val) for val in xpoints]
y_vals = [N(val) for val in ypoints]
fnum = lambdify(x, f, 'numpy')
fxVals = np.linspace(-5,5 ,100)
fyVals = fnum(fxVals)
plt.plot(fxVals, fyVals)
plt.plot(x_vals, y_vals, marker = "o", linestyle = "")

plt.show()