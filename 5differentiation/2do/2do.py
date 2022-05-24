#
# please refer to PPT file
# for exercise
#

import numpy as np

def derivative(f,a,method='central',h=0.01):
    if method == 'centrada':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'progresiva':
        return (f(a + h) - f(a))/h
    elif method == 'regresiva':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")
def f(x):
    return (np.sin(2*x)**3)/((x**4)+1)


print(derivative(f,2.54,method='centrada',h=1e-15))
print(derivative(f,2.54,method='progresiva',h=1e-15))
print(derivative(f,2.54,method='regresiva',h=1e-15))