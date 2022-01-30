import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

df=pd.read_csv("SAW_USL_2.csv")
s1=df["Ne"]*df["Pe"]
s2=df["Nw"]*df["Pw"]
s3=df["Nn"]*df["Pn"]
s4=df["Ns"]*df["Ps"]

# Parameters to set
mu_x = 2.00*s1.sum()-1.75*s2.sum()
variance_x = (2.00*s1.std())**2 + (1.75*s2.std())**2 + 2*(2.00)*(-1.75)*s1.cov(s2)
mu_y = 1.50*s3.sum()-1.25*s4.sum()
variance_y = (1.50*s3.std())**2 + (1.25*s4.std())**2 + 2*(1.50)*(-1.25)*s3.cov(s4)
cov_xy= (2.00*1.50*s1.cov(s3)) - (2.00*1.25*s1.cov(s4)) - (1.75*1.50*s2.cov(s3)) + (1.75*1.25*s2.cov(s4))

# Displaying mean and variance of BND
print("Mean Displacement = (",mu_x,",",mu_y,")")
print("Var(Sx) = ",variance_x,",Var(Sy) = ",variance_y)
print("Cov(Sx,Sy) = ",cov_xy)

# Create grid and Bivariate Normal Distribution(BND)
x = np.linspace(332,345,1000)
y = np.linspace(27,30, 1000)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y
rv = multivariate_normal([mu_x, mu_y], [[variance_x, cov_xy], [cov_xy, variance_y]])

# Make a 3D plot of Probability Density Function(PDF) for BND
fig = plt.figure()
ax= fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
ax.set_title("PDF for Unequal Stepsize")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
plt.show()