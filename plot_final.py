# overlay graphs of baseline 
import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd



df_clp_10 = pd.read_csv( './lb7_data/clp10.csv')
df_clp_10_zoom = pd.read_csv( './lb7_data/clp10_.csv')


df_base= pd.read_csv( './lb7_data/base.csv')
df_base_zoom = pd.read_csv( './lb7_data/base2.csv')
df_sbh= pd.read_csv( './lb7_data/sbh.csv')


# plot baseline full waveform 

# df_list = [
#     df_clp_10,
#     df_clp_10_zoom, 
#     df_base, 
#     df_base_zoom
# ]

def format_df(df): 
    # grab timesteps, start time
    time_increment = df.loc[0, 'Increment']
    time_start = df.loc[0, 'Start']
    df = df.drop(0, axis = 0)
    # remove extraneous columns and rows
    df = df.drop('Start', axis = 1)
    df = df.drop('Increment', axis = 1)
    df = df.drop(df.columns[-1], axis = 1) # last col, unnamed

    df['X'] = (time_increment * df['X'].astype(float)) # x is now time
    # df['CH1'] = df['CH1'].astype(float)
    # df['CH2'] = df['CH2'].astype(float)
    df['CH3'] = df['CH3'].astype(float)
    df['CH4'] = df['CH4'].astype(float)

    if set(['CH1']).issubset(df.columns):
        df['CH1'] = df['CH1'].astype(float)

    return df


df_clp_10 = format_df(df_clp_10)
df_clp_10_zoom = format_df(df_clp_10_zoom)
df_base = format_df(df_base)
df_base_zoom = format_df(df_base_zoom)
df_sbh = format_df(df_sbh)

# df_base.plot(x='X',y='CH4') 
# plt.legend(loc='best')
# plt.title('NMOS Drain Voltage as a function of time')
# plt.xlabel('Time, (seconds)')
# plt.ylabel('NMOS Drain Voltage (volts)')
# # plt.savefig(f'./img_final/Vd_baseline.png')

# df_clp_10_zoom.plot(x='X',y='CH4')
# plt.show()



plt.figure("baseline drain")
plt.plot(
    df_base['X'], df_base['CH4'], 
)

plt.legend(
    ['base',],
    loc='best')
# plt.xscale("log")
plt.title('NMOS Drain Voltage as a function of time')
plt.grid(True, which="both")
plt.xlabel('Time (seconds)')
plt.ylabel('NMOS Drain Voltage (volts)')
plt.savefig(f'./img_final/base.png')
# plt.show()



# PLOT BASE VS CLAMP
# time adjustment 
df_clp_10_zoom['X'] += 3.535e-6

plt.figure("baseline vs clamp")
plt.plot(
    df_base['X'], df_base['CH4'], 
    df_clp_10_zoom['X'],  df_clp_10_zoom['CH4'], 
)

plt.legend(
    ['w/o clamp',
    'w/ clamp',], 
    loc='best')
# plt.xscale("log")
plt.title('NMOS Drain Voltage as a function of time')
plt.grid(True, which="both")
plt.xlabel('Time (seconds)')
plt.ylabel('NMOS Drain Voltage (volts)')
plt.savefig(f'./img_final/base_vs_clamp.png')
# plt.show()


# PLOT BASE vs SNBH
# time adjustment 
df_sbh['X'] -= 7.9e-7

plt.figure("baseline vs sbh")
plt.plot(
    df_base['X'], df_base['CH4'], 
    df_sbh['X'],  df_sbh['CH4'], 
)

plt.legend(
    ['w/o snubber',
    'w/ snubber',], 
    loc='best')
# plt.xscale("log")
plt.title('NMOS Drain Voltage as a function of time')
plt.grid(True, which="both")
plt.xlabel('Time (seconds)')
plt.ylabel('NMOS Drain Voltage (volts)')
plt.savefig(f'./img_final/base_vs_sbh.png')
plt.show()



"""
notes
6.656e-6 - 3.121e-6 = 3.535e-6

7.447e-6 - 6.657e-6
"""