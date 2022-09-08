import math
import numpy as np
import matplotlib.pyplot as plt

a=-30
b=30
m=1000
x=np.linspace(a,b,m)
t=np.linspace(a,b,m)
def f(x):
    return (#math.sin(2*x)+1/3*math.sin(4*x)+1/3*math.sin(8*x)
math.sin(6.5926*x)+math.sin(8.3061*x)+math.sin(4.93883*x)+math.sin(6.3325*x)+math.sin(7.3999*x)
    )
y=[]
z0=np.zeros(m)
z1=[]

for n in range(m):
    y.append(f(x[n]))

def g(x,t):
    return math.cos(x*t)+math.sin(x*t)

for k in range(m):
    for i in range(m):
        z0[i]=(y[i]*g(x[i],t[k]))
    I=0
    for n in range(m):
        I=I+z0[n]/100
        z1.append((I)**4)

a=np.linspace(a,b,len(z1))

fig, aks=plt.subplots(2)
aks[0].set_xlim(-10,10)
aks[0].set_ylim(-3,3)
aks[0].plot(x,y)
aks[1].set_xlim(4,9)
aks[1].set_ylim(0,5)
aks[1].plot(a,z1)
plt.show()