import numpy as np

def SAW():
    n = 500
    n1, n2, n3, n4=[], [], [], []
    x = np.zeros(n+1, dtype=int)
    y = np.zeros(n+1, dtype=int)
    direction= ["East","West","North","South"]
    
    for i in range(1,n+1):
        if i==1:
            step = np.random.choice(direction)
            if step == "East":
                n1.append(step)
                x[i] = x[i-1] + 1
                y[i] = y[i-1]
            elif step == "West":
                n2.append(step)
                x[i] = x[i-1] - 1
                y[i] = y[i-1]
            elif step == "North":
                n3.append(step)
                x[i] = x[i-1]
                y[i] = y[i-1] + 1
            else:
                n4.append(step) 
                x[i] = x[i-1]
                y[i] = y[i-1] - 1


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
            else:
                if step == "East":
                    n1.append(step)
                elif step == "West":
                    n2.append(step)
                elif step == "North":
                    n3.append(step)
                else:
                    n4.append(step) 
    
   
    f1= open("N_East_ESL.txt","a+")
    f1.write(str(len(n1))+"\n")

    f2= open("N_West_ESL.txt","a+")
    f2.write(str(len(n2))+"\n")

    f3= open("N_North_ESL.txt","a+")
    f3.write(str(len(n3))+"\n")

    f4= open("N_South_ESL.txt","a+")
    f4.write(str(len(n4))+"\n")

for i in range(1000):
  SAW()