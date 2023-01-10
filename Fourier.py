import numpy as np 
import matplotlib.pyplot as plt
import math
pi=np.pi 
x = np.linspace(0,4*pi,1000)
limit=10
plt.figure(figsize=(10,7))
#For Square Wave
n = 1;
y = (1/n)*(np.sin (n*x));
z = y;
plt.subplot(321)
plt.plot(y)
plt.grid(True)
plt.title (['frequencies'])
for i in range(3,limit,2):
    y =(1/i)*(np.sin(i*x))
    plt.plot (y)
    z+=y;
plt.subplot(322)
plt.plot(z)
plt.title (['Fourier series for Square wave'])
plt.grid(True)
#For Sawtooth Wave
n=1
y=(1/n)*(np.sin(n*x))
z=y 
plt.subplot(323)
plt.plot(y)
plt.title (['frequencies'])
plt.grid(True)
for i in range(2,limit,1):
    y=(1/i)*(np.sin(i*x))
    plt.plot(y)
    z+=y 
plt.subplot(324)
plt.plot(z)
plt.title (['Fourier series for Sawtooth wave'])
plt.grid(True)
#For Triangular Wave
n=1
y=(1/n**2)*(np.cos(n*x))
z=y
plt.subplot(325)
plt.plot(y)
plt.title (['frequencies'])
plt.grid(True)
for i in range(3,limit,2):
    y=(1/i**2)*(np.cos(i*x))
    plt.plot(y)
    z+=y 
plt.subplot(326)
plt.plot(z)
plt.title (['Fourier series for Triangular wave'])
plt.grid(True)
plt.show()