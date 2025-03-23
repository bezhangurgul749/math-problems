import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0]**2 + 3*x[1]*x[2] - 5

result = minimize(f, [1, 2, 3], method='Nelder-Mead')
print(result.x)
