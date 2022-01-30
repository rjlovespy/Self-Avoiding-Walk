import pandas as pd
import numpy as np

df=pd.read_csv("SAW_ESL_1.csv")

s1 = np.array(df["N_East"])
s2 = np.array(df["N_West"])
s3 = np.array(df["N_North"])
s4 = np.array(df["N_South"])

ne,fe = np.unique(s1, return_counts=True)
pe = np.zeros(len(ne))
for i in range(len(ne)):
    pe[i]=fe[i]/1000
nw,fw = np.unique(s2, return_counts=True)
pw = np.zeros(len(nw))
for i in range(len(nw)):
    pw[i]=fw[i]/1000
nn,fn = np.unique(s3, return_counts=True)
pn = np.zeros(len(nn))
for i in range(len(nn)):
    pn[i]=fn[i]/1000
ns,fs = np.unique(s4, return_counts=True)
ps = np.zeros(len(ns))
for i in range(len(ns)):
    ps[i]=fs[i]/1000

Ne,Nw,Nn,Ns=0,0,0,0  
for i in range(len(ne)):
    Ne+=ne[i]*pe[i]
for i in range(len(nw)):
    Nw+=nw[i]*pw[i]
for i in range(len(nn)):
    Nn+=nn[i]*pn[i]
for i in range(len(ns)):
    Ns+=ns[i]*ps[i]

print("Mean Displacement = (",Ne-Nw,", ",Nn-Ns,")")