import numpy as np
import matplotlib.pyplot as plt

f = lambda x : x**2 - 4*x +6
x = np.linspace(-1,6,100)
y = f(x)

# 그리기
plt.plot(x, y, 'k-') #k-
plt.plot(2,2,'sk') #sk
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()