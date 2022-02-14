import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Parameters to set
mu_x = -6.830
mu_y = -7.978
variance_x = 0.088
variance_y = 0.110
cov_xy = 0.015

# Create grid and Bivariate Normal Distribution(BND)
x = np.linspace(-7.7,-5.9,1000)
y = np.linspace(-8.9,-7.1,1000)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y
rv = multivariate_normal([mu_x, mu_y], [[variance_x, cov_xy], [cov_xy, variance_y]])

# Make a 3D plot of Probability Density Function(PDF) for BND
fig = plt.figure()
ax= fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
ax.set_title("PDF for Equal Stepsize: s=(-6.830,-7.978)")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
fig.tight_layout()
plt.show()