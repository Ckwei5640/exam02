import numpy as np
import matplotlib.pyplot as plt
import serial
import time

serdev = '/dev/ttyACM0'

t = np.arange(0,10,0.1) # 0s~10s, every 0.1S

s = serial.Serial(serdev,baudrate = 115200)

x = np.arange(0,10,0.1)
y = np.arange(0,10,0.1)
z = np.arange(0,10,0.1)
largerthan5 = np.arange(0,10,0.1)

for i in range(100):
    line = s.readline()

    x[i] = line.split()[0]
    y[i] = line.split()[1]
    z[i] = line.split()[2]
    largerthan5[i] = line.split()[3]

fig,ax = plt.subplots(2,1)
for i in range(100):
    ax[1].plot([t[i],t[i]],[0,largerthan5[i]],color = "red",linewidth = 2.5,linestyle = "-")
    ax[1].scatter([t[i],],[largerthan5[i],],50,color = "blue")

plt.yticks([0,+1])
ax[0].plot(t,x,color = "blue",linewidth = 2.5,linestyle = "-",label = "x")
ax[0].plot(t,y,color = "red",linewidth = 2.5,linestyle = "-",label = "y")
ax[0].plot(t,z,color = "green",linewidth = 2.5,linestyle = "-",label = "z")
ax[0].legend(loc = 'best')
plt.show()