import random
import matplotlib.pyplot as plt
  
  
# store the random numbers in a 
# list
nums = []
low = 10
high = 100
mode = 20
  
for i in range(100):
    temp = random.betavariate(5, 10)
    nums.append(temp)
      
# plotting a graph
plt.plot(nums)
plt.show()