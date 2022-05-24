#
# OPTIONAL
# requires installing stats
#
# select a distribution from stats
# produce random numbers on such a distribution
# 
# zeeAlso
# en.wikipedia.org/wiki/Probability_distribution
#

import numpy as np
from scipy.stats import alpha
import matplotlib.pyplot

a, b = 5, 2
values = alpha.rvs(a, b, size=1000)
print(values)
matplotlib.pyplot.hist(values)
matplotlib.pyplot.show()