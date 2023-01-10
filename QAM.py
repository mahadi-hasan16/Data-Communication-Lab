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
plt.subplot(311)
plt.plot(sig,color='r')
plt.title(b)
plt.axhline(y=0.5,color='k')
c1=5*np.sin(2*pi*f*t)
c2=2*np.sin(2*pi*f*t)
plt.subplot(312)
plt.plot(c1,label='Carrier 1(High Amplitude)')
plt.plot(c2,label='Carrier 2(Low Amplitude)')
plt.legend()
plt.axhline(y=0,color='k')
for i in range(len(sig)):
    if sig[i]==0:
        t[i]=t[i]+1/(4*f)
y=[] #To sto the value of QAM signal
for i in range(len(sig)):
    if sig[i]==1:
        y.append(5*np.sin(2*pi*f*t[i]))
    else:
        y.append(2*np.sin(2*pi*f*t[i]))
plt.subplot(313)
plt.plot(y)
plt.axhline(y=0,color='k')
plt.show()
