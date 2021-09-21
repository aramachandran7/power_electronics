import matplotlib.pyplot as plt
from numpy import arange
# parse logfile

f = open('./logfiles/log20W.txt', 'r')
Lines = f.readlines()
Lines = Lines
top = []
btm = []

for line in Lines:
    sp = line.split()
    if len(sp)> 1:
        btm.append(float(sp[0][12:-1]))
        top.append(float(sp[1][9:-1]))

time = arange(0.0, float(len(top))/2, .5)
time /= 60

plt.plot(time, btm, label = 'Thermistor on Heatsink')
plt.plot(time, top, label = 'Thermistor on Power Resistor')
plt.ylabel('temperature, degrees C')
plt.xlabel('time, minutes')
plt.title('20W dissipated over resistor over 30 minutes')
plt.legend(loc='lower right')
plt.show()
