import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal
bit_len=16
pi=np.pi 
b=[1,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0]
sig=np.zeros(bit_len*len(b))
for i in range(len(b)):
	if b[i]==1:
		sig[bit_len*i:bit_len*(i+1)]=1
plt.figure(figsize=(10,5))
plt.subplot(311)
plt.plot(sig,color='r')
plt.title(b)
plt.axhline(y=0.5,color='k')
fc=5000
t=np.linspace(0,0.01,len(sig),endpoint=True)
c=np.sin(2*pi*fc*t)
plt.subplot(312)
plt.plot(c)
plt.axhline(y=0,color='k')
ask=sig*c
plt.subplot(313)
plt.plot(ask)
plt.axhline(y=0,color='k')
plt.show()
