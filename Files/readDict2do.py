#
# read binary file (dictionary)
# and print it
#

import pickle


with open('dict.pickle', 'rb') as f:
     data = pickle.load(f)

print (data)