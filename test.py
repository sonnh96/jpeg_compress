import numpy as np
import matplotlib.pyplot as plt

# Construct lines
# x > 0
x = np.linspace(0, 100, 2000)
# y >= 2
y1 = x*0
# 2y <= 25 - x
y2 = (1000-10*x)/250

y3 = (2**21-40*x)/160


# Make plot
plt.plot(x, y1, label=r'$y\geq0$')
plt.plot(x, y2, label=r'$250y\leq1000-10x$')
plt.plot(x, y3, label=r'$160y\leq 2^21 - 40x$')

#plt.plot(x, y4, label=r'$y\leq 2x-5$')
plt.xlim((0, 120))
plt.ylim((0, 10))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

# Fill feasible region
# y5 = np.minimum(y2, y4)
# y6 = np.maximum(y1, y3)
plt.fill_between(x, y2, color='grey')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.show()