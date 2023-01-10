import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal
bit_len=32
pi=np.pi 
f=5000
b=[1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1]
sig=np.zeros(bit_len*len(b))
for i in range(len(b)):
    if b[i]==1:
        sig[bit_len*i:bit_len*(i+1)]=1
t=np.linspace(0,0.01,len(sig),endpoint=True)
plt.figure(figsize=(10,6))
plt.suptitle("PSK")
plt.subplot(411)
plt.plot(sig,color='r')
plt.title(b)
plt.axhline(y=0.5,color='k')
c1=np.sin(2*pi*f*t)
plt.subplot(412)
plt.plot(c1)
plt.axhline(y=0,color='k')
c2=np.sin(2*pi*f*t+pi)
plt.subplot(413)
plt.plot(c2)
plt.axhline(y=0,color='k')
for i in range(len(sig)):
    if sig[i]==0:
        t[i]=(-1)*t[i]
y=np.sin(2*f*pi*t)
plt.subplot(414)
plt.plot(y)
plt.axhline(y=0,color='k')
plt.show()
