#
# convert 1st variable as tuple
# convert 2nd variable as dictionary
# convert 3rd variable as list
#
from math import prod
import pandas as pd
iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')
#vs
#iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data')

print('head',iris.head())
lista = iris['sepal length'].tolist()

tupla = tuple(iris['sepal width'])

list = range(1,151)
dictionary = dict(iris['petal length'])
print(lista)
print(tupla)
print(dictionary)