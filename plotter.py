import matplotlib.pyplot as plt
from numpy import arange
# parse logfile

f = open('./logfiles/log20W.txt', 'r')
Lines = f.readlines()
Lines = Lines
top = []
btm = []

print(Lines[0].split())
print(Lines[1].split())
print(float(Lines[2].split()[0][12:-1]))
print(float(Lines[2].split()[1][9:-1]))
for line in Lines:
    sp = line.split()
    if len(sp)> 1:
        btm.append(float(sp[0][12:-1]))
        top.append(float(sp[1][9:-1]))

time = arange(0.0, float(len(top))/2, .5)
print(len(time), len(top), len(btm))

plt.plot(time, btm, time, top)
plt.ylabel('temperature, degrees C')
plt.xlabel('time, seconds')

plt.show()
