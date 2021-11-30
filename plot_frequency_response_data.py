import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
# parse logfile

df_1_5 = pd.read_csv(  './lb9_data/LB9_1.5V.csv')
df_1_75 = pd.read_csv( './lb9_data/LB9_1.75V.csv')
df_1_95 = pd.read_csv( './lb9_data/LB9_1.95V.csv')
df_2_25 = pd.read_csv( './lb9_data/LB9_2.25V.csv')

df_list = [
df_1_5 ,
df_1_75,
df_1_95,
df_2_25,
]

title_list = [
'1.5 V',
'1.75 V',
'1.95 V',
'2.25 V',    
]


# hand recorded dc offset data 

d = {'offset': [1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3], 'output_rms': [3.899, 4.806, 5.716, 6.63, 7.54, 8.46, 9.37, 10.24], 'vsh_peak': [136, 170, 204, 230, 264, 294, 328, 360]}
df_dc_offset = pd.DataFrame(data=d)

plt.scatter(
    df_dc_offset['offset'],  df_dc_offset['output_rms'], 
)
plt.title('Output Voltage as a function of Vcomp DC offset')
plt.xlabel('DC Offset (V)')
plt.ylabel('Output Voltage (V)')
plt.savefig(f'./figs_lb9/dc_offset_output_v.png')
plt.show()

plt.scatter(
    df_dc_offset['offset'],  df_dc_offset['vsh_peak'], 
)
plt.title('Peak shunt voltage as a function of Vcomp DC offset')
plt.xlabel('DC Offset (V)')
plt.ylabel('Peak shunt voltage (mV)')
plt.savefig(f'./figs_lb9/dc_offset_peak_shunt.png')
plt.show()


# waveforms data handling
for i,df in enumerate(df_list):

    # # grab timesteps, start time
    # time_increment = df.loc[0, 'Increment']
    # time_start = df.loc[0, 'Start']
    # df = df.drop(0, axis = 0)
    # # remove extraneous columns and rows
    # df = df.drop('Start', axis = 1)
    # df = df.drop('Increment', axis = 1)
    # df = df.drop(df.columns[-1], axis = 1) # last col, unnamed

    # df['X'] = time_increment * df['X'].astype(float) # x is now time
    # df['CH1'] = df['CH1'].astype(float)
    # df['CH2'] = df['CH2'].astype(float)
    df['Frequency (Hz)'] = df['Frequency (Hz)'].astype(float)
    df['Channel 1 Magnitude (dB)'] = df['Channel 1 Magnitude (dB)'].astype(float)
    df['Channel 2 Magnitude (dB)'] = df['Channel 2 Magnitude (dB)'].astype(float)
    df['Channel 2 Phase (*)'] = df['Channel 2 Phase (*)'].astype(float)

# CH1 Magnitude 
# plt.plot(
#     df_1_5['Frequency (Hz)'],  df_1_5['Channel 1 Magnitude (dB)'], 
#     df_1_75['Frequency (Hz)'], df_1_75['Channel 1 Magnitude (dB)'], 
#     df_1_95['Frequency (Hz)'], df_1_95['Channel 1 Magnitude (dB)'], 
#     df_2_25['Frequency (Hz)'], df_2_25['Channel 1 Magnitude (dB)'], 

# )
# plt.legend(
#     ['1.5 V',
#     '1.75 V',
#     '1.95 V',
#     '2.25 V',],    
#     loc='best')
# plt.title('Channel 1 Magnitude')
# plt.xscale("log")
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (dB)')
# plt.savefig(f'./figs_lb9/CH1Mag.png')
# plt.show()


# df.plot(x='Frequency (Hz)',y='Channel 1 Magnitude (dB)')
# plt.legend(loc='best')
# plt.title('Channel 1 Magnitude, Vcomp offset = ' + title_list[i])
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (dB)')
# plt.savefig(f'./figs_lb9/CH1Mag_{title_list[i]}.png')

# # CH2 Magnitude 
plt.figure("CH2 Mags")
plt.plot(
    df_1_5['Frequency (Hz)'],  df_1_5['Channel 2 Magnitude (dB)'], 
    df_1_75['Frequency (Hz)'], df_1_75['Channel 2 Magnitude (dB)'], 
    df_1_95['Frequency (Hz)'], df_1_95['Channel 2 Magnitude (dB)'], 
    df_2_25['Frequency (Hz)'], df_2_25['Channel 2 Magnitude (dB)'], 

)
plt.legend(
    ['1.5 V',
    '1.75 V',
    '1.95 V',
    '2.25 V',],    
    loc='best')
plt.xscale("log")
plt.title('Channel 2 Magnitude')
plt.grid(True, which="both")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.savefig(f'./figs_lb9/CH2Mag.png')

# df.plot(x='Frequency (Hz)',y='Channel 2 Magnitude (dB)')
# plt.legend(loc='best')
# plt.title('Channel 2 Magnitude, Vcomp offset = ' + title_list[i])
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (dB)')
# plt.savefig(f'./figs_lb9/CH1Mag_{title_list[i]}.png')

plt.figure("CH2 Phases")
# # CH2 Phase  
plt.plot(
    df_1_5['Frequency (Hz)'],   df_1_5['Channel 2 Phase (*)'], 
    df_1_75['Frequency (Hz)'], df_1_75['Channel 2 Phase (*)'], 
    df_1_95['Frequency (Hz)'], df_1_95['Channel 2 Phase (*)'], 
    df_2_25['Frequency (Hz)'], df_2_25['Channel 2 Phase (*)'], 

)
plt.legend(
    ['1.5 V',
    '1.75 V',
    '1.95 V',
    '2.25 V',],    
    loc='best')
plt.title('Channel 2 Phase')
plt.xscale("log")
plt.grid(True, which="both")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.savefig(f'./figs_lb9/CH2Phase.png')
plt.show()

# # try: # channel 4
# df.plot(x='Frequency (Hz)',y='Channel 2 Phase (*)')
# plt.legend(loc='best')
# plt.title('Channel 2 Phase, Vcomp offset = ' + title_list[i])
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Phase (degrees)')
# plt.savefig(f'./figs_lb9/CH1Mag_{title_list[i]}.png')


plt.show()
