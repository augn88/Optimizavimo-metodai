from sympy import symbols, N, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')
a = 7
b = 6
f = ((x**2 - a)**2) / b - 1

epsilon = 10**-4
right = 10
left = 0
xm = (right + left) / 2
difference = right - left
fxm = f.subs(x, xm)
iteration = 0
index = 0
xpoints = []
ypoints = []

while difference > epsilon:
    x1 = left + difference / 4
    x2 = right - difference / 4
    fx1 = f.subs(x, x1)
    fx2 = f.subs(x, x2)
    if fx1 < fxm:
        right = xm
        xm = x1
    elif fx2 < fxm:
        left = xm
        xm = x2
    else:
        left = x1
        right = x2
    fxm = f.subs(x, xm)
    difference = right - left
    iteration += 1
    xpoints.append(xm)
    print(f"{iteration}:\tK = {N(left):.4f} xm = {N(xm):.4f} D = {N(right):.4f}")

while len(xpoints) != len(ypoints):     
   ypoints.append(N(f.subs(x, xpoints[index])))
   index += 1
x_vals = [N(val) for val in xpoints]
y_vals = [N(val) for val in ypoints]
fnum = lambdify(x, f, 'numpy')
fxVals = np.linspace(0,3 ,100)
fyVals = fnum(fxVals)

plt.plot(fxVals, fyVals)
plt.plot(x_vals, y_vals, marker = "o", linestyle = "")

plt.show()

print(f"Vidurio taškas {N(xm):.4f}")