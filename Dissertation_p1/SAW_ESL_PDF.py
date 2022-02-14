import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

df=pd.read_csv("SAW_ESL_2.csv")
s1=df["Ne"]*df["Pe"]
s2=df["Nw"]*df["Pw"]
s3=df["Nn"]*df["Pn"]
s4=df["Ns"]*df["Ps"]

# Parameters to set
mu_x = s1.sum()-s2.sum()
variance_x = s1.std()**2 + s2.std()**2 - 2*s1.cov(s2) 
mu_y = s3.sum()-s4.sum()
variance_y = s3.std()**2 + s4.std()**2 - 2*s3.cov(s4) 
cov_xy= s1.cov(s3)-s1.cov(s4)-s2.cov(s3)+s2.cov(s4)

# Displaying mean and variance of BND
print("Mean Displacement = (",mu_x,",",mu_y,")")
print("Var(Sx) = ",variance_x,",Var(Sy) = ",variance_y)
print("Covariance(Sx,Sy) = ",cov_xy)

# Create grid and Bivariate Normal Distribution(BND)
x = np.linspace(-0.5,1.4,1000)
y = np.linspace(9,13,1000)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y
rv = multivariate_normal([mu_x, mu_y], [[variance_x, cov_xy], [cov_xy, variance_y]])

# Make a 3D plot of Probability Density Function(PDF) for BND
fig = plt.figure()
ax= fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, rv.pdf(pos),cmap='viridis',linewidth=0)
ax.set_title("PDF for Equal Stepsize")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
fig.tight_layout()
plt.show()