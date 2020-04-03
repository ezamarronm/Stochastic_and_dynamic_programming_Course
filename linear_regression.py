import matplotlib.pyplot as plt
import numpy as np
x = np.array([2.5,7.5,15,30,1*60,2*60,4*60,8*60,16*60])
y = np.array([40,96,173,311,560,1008,1814,3265,5877])

coeffs = np.polyfit(x,y,1)
print(coeffs)

m = coeffs[0]
b = coeffs[1]
estimate_y = m*x + b

plt.plot(x, estimate_y)
plt.scatter(x,y)
plt.show