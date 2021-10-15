import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
# parse logfile

df_4 = pd.read_csv( './flyback_data/4v.csv')
df_4o = pd.read_csv('./flyback_data/4vo.csv')
df_7 = pd.read_csv( './flyback_data/7vo.csv')
df_7o = pd.read_csv('./flyback_data/7vo2.csv')
df_9 = pd.read_csv( './flyback_data/9v.csv')
df_9o = pd.read_csv('./flyback_data/9vo.csv')

df_list = [
    df_4, 
    df_4o,
    df_7,
    df_7o,
    df_9,
    df_9o,
]

title_list = [
    '4V ', 
    '4V (zoom)',
    '7V ',
    '7V (zoom)',
    '9V' ,
    '9V (zoom)',
]
for i,df in enumerate(df_list):

    # grab timesteps, start time
    time_increment = df.loc[0, 'Increment']
    time_start = df.loc[0, 'Start']
    df = df.drop(0, axis = 0)
    # remove extraneous columns and rows
    df = df.drop('Start', axis = 1)
    df = df.drop('Increment', axis = 1)
    df = df.drop(df.columns[-1], axis = 1) # last col, unnamed

    df['X'] = time_increment * df['X'].astype(float) # x is now time
    df['CH1'] = df['CH1'].astype(float)
    df['CH2'] = df['CH2'].astype(float)
    df['CH3'] = df['CH3'].astype(float)
    df['CH4'] = df['CH4'].astype(float)


    # plot CH1
    df.plot(x='X',y='CH1')
    plt.legend(loc='best')
    plt.title('Voltage across shunt resistor as a function of time, output voltage = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('Voltage across shunt resistor, (volts)')

    # plot CH2
    df.plot(x='X',y='CH2')
    plt.legend(loc='best')
    plt.title('NMOS Drain Voltage as a function of time, output  voltage = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('NMOS Drain Voltage (volts)')

    # try: # channel 3
    df.plot(x='X',y='CH3')
    plt.legend(loc='best')
    plt.title('Output Voltage as a function of time, output voltage RMS = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('Output Voltage (volts)')
    # except: 
    #     print(title_list[i] + ' does not have output voltage logged')

    # try: # channel 4
    df.plot(x='X',y='CH4')
    plt.legend(loc='best')
    plt.title('Input Voltage as a function of time, output voltage RMS = ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('Input Voltage (volts)')
    # except: 
    #     print(title_list[i] + ' does not have input voltage logged')
    

plt.show()
