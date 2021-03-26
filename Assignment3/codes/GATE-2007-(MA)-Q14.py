#assignment 3

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import semicircular
k = 10000

count = 0

data_x = semicircular.rvs(loc = 0, scale = 1, size = k, random_state = None)
data_y = semicircular.rvs(loc = 0, scale = 1, size = k, random_state = None)
for i in range(k):
  for j in range(k):
    #print(" " + str(data_y[j]) + ":" + str(data_x[i]))
    if (data_y[j] > abs(data_x[i])):
      count = count + 1

probab = count/pow(k,2)
print("The probability is: ", probab)

#plotting

cases = ['']

probab_theo = 0.25
probab_sim = probab

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])
plt.legend()
plt.show()