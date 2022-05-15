#
# 2do
#

import pickle


t=12,True,3.1,'aCat'
print (t)
with open('data.pickle', 'wb') as f:
    pickle.dump(t, f)