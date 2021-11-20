import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

X = np.linspace(0,4,100)
Y = np.random.random(len(X))
YS = []

for _ in range(1000):
    Y = X * Y * (1-Y) 

for _ in range(100):
    Y = X * Y * (1-Y) 
    YS.append(Y)

for  Y in YS:
     plt.scatter(X,Y,s=0.1, c='#000')
# #plt.scatter(X, Y, s=1,c ='#5dbb63') 
plt.axis("off")

print("--- %s seconds ---" % (time.time() - start_time))  
plt.show()