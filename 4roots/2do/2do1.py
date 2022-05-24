#
# please refer to PPT file
# for exercise
#
from cmath import e
import numpy
p = lambda x: e**(2-x)-(7*x)
Dp = lambda x: -e**(2-x)-7

x = numpy.linspace(0,10,1000)
dx = -e**(2-x)-7
y = e**(2-x)-(7*x)
dydx = numpy.gradient(y, dx)
print(dydx)