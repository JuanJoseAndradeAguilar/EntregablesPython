from math import cos, exp, pi, sin, sqrt
from scipy.integrate import quad

def f(x):
    return 2*sin(sqrt(x))-x

res, err = quad(f, 0, 1.9724)

print("{:f}".format(res))

from math import cos, exp, pi
from scipy.integrate import quad

def f(x):
    return (7**(-x))+3

res, err = quad(f, -1, 2)

print("{:f}".format(res))