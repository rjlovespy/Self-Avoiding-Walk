import matplotlib.pyplot as plt
import numpy as np

def SAW():
    n=50
    sl=2
    x = np.zeros(n+1, dtype=int)
    y = np.zeros(n+1, dtype=int)
    direction= ["East","West","North","South"]

    for i in range(n+1):
        if i==0:
            continue
        else:
            step = np.random.choice(direction)
            if step == "East":
                x[i] = x[i-1] + sl
                y[i] = y[i-1]
            elif step == "West":
                x[i] = x[i-1] - sl
                y[i] = y[i-1]       
            elif step == "North":
                x[i] = x[i-1] 
                y[i] = y[i-1] + sl     
            else:
                x[i] = x[i-1] 
                y[i] = y[i-1] - sl
       
            while (x[i] in x[:i-1]) and (y[i] in y[:i-1]):
                step = np.random.choice(direction)
                if step == "East":
                    x[i] = x[i-1] + sl
                    y[i] = y[i-1]
                elif step == "West":
                    x[i] = x[i-1] - sl
                    y[i] = y[i-1]          
                elif step == "North":
                    x[i] = x[i-1] 
                    y[i] = y[i-1] + sl       
                else:
                    x[i] = x[i-1] 
                    y[i] = y[i-1] - sl
                                        

    fig= plt.figure()
    ax= fig.add_subplot()                
    ax.plot(x,y, color="blue")
    ax.scatter(x[0],y[0],color="black", label="Start")
    ax.scatter(x[-1],y[-1], color="red", label="End")
    t=np.linspace(0,2*np.pi,361)
    ax.plot(50*np.cos(t),50*np.sin(t), color="lime", label="Wine Shop")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_title("When each step length is of 2 unit")
    ax.grid(which="major")
    ax.grid(which="minor", linestyle="--")
    ax.minorticks_on()
    fig.suptitle("For 50 Steps")
    plt.legend()
    plt.show()

SAW()