import matplotlib.pyplot as plt
import numpy as np

def SAW():
    n=200
    x = np.zeros(n+1, dtype=int)
    y = np.zeros(n+1, dtype=int)
    direction= ["East","West","North","South"]

    for i in range(n+1):
        if i==0:
            continue
        else:
            step = np.random.choice(direction, p=[0.2,0.6,0.1,0.1])
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
       
            while (x[i] in x[:i-1]) and (y[i] in y[:i-1]):
                step = np.random.choice(direction,p=[0.2,0.6,0.1,0.1])
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
                                        

    fig= plt.figure()
    ax= fig.add_subplot()                
    ax.plot(x,y, color="blue")
    ax.scatter(x[0],y[0],color="lime", label="Start")
    ax.scatter(x[-1],y[-1], color="red", label="End")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_title("When p=[0.2,0.6,0.1,0.1]")
    ax.grid(which="major")
    ax.grid(which="minor", linestyle="--")
    ax.minorticks_on()
    fig.suptitle("Self Avoiding Walk of 200 Steps")
    fig.tight_layout()
    plt.legend()
    plt.show()

SAW()