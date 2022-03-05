import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import numpy as np

direction= ["East","West","North","South"]
n = 200
x = np.zeros(n+1, dtype=int)
y = np.zeros(n+1, dtype=int)

for i in range(n+1):
    if i==0:
      continue 
    else:
      step = np.random.choice(direction)
      if step == "East":
        x[i] = x[i-1] + 1
        y[i] = y[i-1]
      elif step == "West":
        x[i] = x[i-1] - 1
        y[i] = y[i-1]
      elif step == "North":
        x[i] = x[i-1]
        y[i] = y[i-1] + 1
      else:
        x[i] = x[i-1]
        y[i] = y[i-1] - 1  
    
      while ((x[i] in x[:i-1]) and (y[i] in y[:i-1])):
        step = np.random.choice(direction)
        if step == "East":
          x[i] = x[i-1] + 1
          y[i] = y[i-1]
        elif step == "West":
          x[i] = x[i-1] - 1
          y[i] = y[i-1]
        elif step == "North":
          x[i] = x[i-1]
          y[i] = y[i-1] + 1
        else:
          x[i] = x[i-1]
          y[i] = y[i-1] - 1


fig=plt.figure()
ax=fig.add_subplot()
ax=plt.axes(xlim=(min(x)-1, max(x)+1), ylim=(min(y)-1, max(y)+1))
sarw1, =ax.plot([], [],'b', label= "For 200 Steps")
walker1, =ax.plot([], [], 'r*', markersize =18, label="Drunkard")
position1, =ax.plot([], [],'mo',markersize=3)

def SARW(i):
  sarw1.set_data(x[:i+1], y[:i+1])
  walker1.set_data(x[i], y[i])
  position1.set_data(x[:i+1], y[:i+1])
  return sarw1, walker1, position1, 

anim= animation.FuncAnimation(fig, SARW, frames=n+1,interval=100,blit=True,repeat =False)

fig.patch.set_facecolor("lime")
fig.tight_layout()
fig.suptitle("Self Avoiding Random Walk in 2D")
plt.axis(False)
plt.legend()
plt.show()