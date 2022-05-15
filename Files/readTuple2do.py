#
# read binary file (tuple)
# and print it
#

import pickle


with open('data.pickle', 'rb') as f:
     data = pickle.load(f)

print (data)