#
# radious of circle inscribed in a triangle
# place here your solution code
#
# zeeAlso
# https://keisan.casio.com/exec/system/1223428152

from math import sqrt


a = 8
b = 10
c = 15

s = .5 * (a+b+c)
print (s)

r = sqrt(s*(s-a)*(s-b)*(s-c))/s
print (r)