#
# 2do
#


import pickle


d={'one':'aaa aaa', 'two':'bbb bbb', 'three':'ccc ccc'}
print (d)
with open('dict.pickle', 'wb') as f:
    pickle.dump(d, f)