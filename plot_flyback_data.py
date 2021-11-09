import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
# parse logfile

df_base= pd.read_csv( './lb7_data/base.csv')
df_base_zoom = pd.read_csv( './lb7_data/base2.csv')
df_clp_8 = pd.read_csv( './lb7_data/clp8_.csv')
df_clp_8_zoom = pd.read_csv( './lb7_data/clp8.csv')
df_clp_10 = pd.read_csv( './lb7_data/clp10.csv')
df_clp_10_zoom = pd.read_csv( './lb7_data/clp10_.csv')
df_sbh= pd.read_csv( './lb7_data/sbh.csv')
df_sbh_zoom = pd.read_csv( './lb7_data/sbh2.csv')
df_sbl = pd.read_csv('./lb7_data/sbl62.csv')
df_sbl_zoom = pd.read_csv( './lb7_data/sbl62_.csv')

# df_list = [
#     df_4, 
#     df_4o,
#     df_7,
#     df_7o,
#     df_9,
#     df_9o,
# ]

df_list = [
    df_base     , 
df_base_zoom, 
df_clp_8, 
df_clp_8_zoom, 
df_clp_10, 
df_clp_10_zoom, 
df_sbh, 
df_sbh_zoom, 
df_sbl, 
df_sbl_zoom, 
]

# title_list = [
#     '4V', 
#     '4V_zoom',
#     '7V',
#     '7V_zoom',
#     '9V' ,
#     '9V_zoom',
# ]

title_list = [
'baseline', 
'baseline zoomed', 
'clamp 8V', 
'clamp 8V zoomed', 
'clamp 10V', 
'clamp 10V zoomed', 
'snubber high frequency', 
'snubber high frequency zoomed', 
'snubber low frequency ', 
'snubber low frequency zoomed', 
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
    # df['CH1'] = df['CH1'].astype(float)
    # df['CH2'] = df['CH2'].astype(float)
    df['CH3'] = df['CH3'].astype(float)
    df['CH4'] = df['CH4'].astype(float)

    
    # plot CH1
    # df.plot(x='X',y='CH1')
    # plt.legend(loc='best')
    # plt.title('Voltage across shunt resistor as a function of time, output voltage = ' + title_list[i])
    # plt.xlabel('Time, (seconds)')
    # plt.ylabel('Voltage across shunt resistor, (volts)')
    # # plt.axis([x_min, x_max, y_min, y_max])
    # plt.savefig(f'./figs_lb6/Vsh_{title_list[i]}.png')


    # df.iloc[int(len(df.index)/2):int(len(df.index)*3/4)].plot(x='X',y='CH1')
    # plt.legend(loc='best')
    # plt.title('Voltage across shunt resistor as a function of time, output voltage = ' + title_list[i])
    # plt.xlabel('Time, (seconds)')
    # plt.ylabel('Voltage across shunt resistor, (volts)')
    # plt.savefig(f'./figs_lb6/Vsh_{title_list[i]}.png')

    if set(['CH1']).issubset(df.columns):
        df['CH1'] = df['CH1'].astype(float)

        # df['CH2'] = df['CH2'].astype(float)

        # plot ch2 for diode cathode
        # plot CH2
        df.plot(x='X',y='CH1')
        plt.legend(loc='best')
        plt.title('Clamp Diode Cathode Voltage as a function of time, ' + title_list[i])
        plt.xlabel('Time, (seconds)')
        plt.ylabel('NMOS Drain Voltage (volts)')
        plt.savefig(f'./figs_lb7/Vcathode_{title_list[i]}.png')

    # try: # channel 3
    df.plot(x='X',y='CH3')
    plt.legend(loc='best')
    plt.title('Voltage across shunt resistor as a function of time, ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('Shunt Voltage (volts)')
    plt.savefig(f'./figs_lb7/Vsh_{title_list[i]}.png')
    # except: 
    #     print(title_list[i] + ' does not have output voltage logged')

    # try: # channel 4
    df.plot(x='X',y='CH4')
    plt.legend(loc='best')
    plt.title('NMOS Drain Voltage as a function of time, ' + title_list[i])
    plt.xlabel('Time, (seconds)')
    plt.ylabel('NMOS Drain Voltage (volts)')
    plt.savefig(f'./figs_lb7/Vd_{title_list[i]}.png')
    # except: 
    #     print(title_list[i] + ' does not have input voltage logged')
    # if i>2: 
    #     break
    

plt.show()
