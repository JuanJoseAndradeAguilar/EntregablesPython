from matplotlib import pyplot
import numpy
import matplotlib

data = numpy.random.normal(1000,1000,5000)
print(data)
pyplot.hist(data)
pyplot.show()