# -*- coding: utf-8 -*-
"""
MANDELBROT SET

By: it's literally monique
"""
# import libraries needed for program
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

# initialize rows, columns and iterations
rows = 2000
cols = 2000
iterations = 200

# function that will calculate the specific values in the mandelbrot set
def mandelbrot(c, z):
    global iterations
    count = 0
    for a in range(iterations):
        z = z**2 + c
        count += 1
        if(abs(z) > 4):
            break
    return count

# function that will create the mandelbrot set
def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            z = complex(0, 0)
            count = mandelbrot(c, z)
            m[i, j] = count
    return m

# create our x and y coordinates using numpy
x = np.linspace(-2, 1, rows)
y = np.linspace(-1, 1, cols)

# create our mandelbrot set
m = mandelbrot_set(x, y)

# show the set (best colors: binary, hot, bone, magma)
T = m.T
T = np.log(T)
plt.imshow(T, cmap = "hot")
plt.axis("off")
#plt.savefig('mandelbrot_set.png', dpi=300, bbox_inches='tight')
print("--- %s seconds ---" % (time.time() - start_time))  
plt.show()
