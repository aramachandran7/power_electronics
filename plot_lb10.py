import matplotlib.pyplot as plt
from numpy import arange
import pandas as pd
# parse logfile

"""
#Digilent WaveForms Network Analyzer - Bode
#Device Name: Discovery2
#Serial Number: SN:210321A18885
#Date Time: 2021-12-02 10:56:32.289
#Start: 100 Hz
#Stop: 50000 Hz
#Steps: 151
#Wavegen: Wavegen1
#Amplification: 1 X
#Settle: 10 ms
#MinPeriods: 16 
#Channel: Channel 2
#Range: 60.4918 V
#Offset: -0.00337698 V
#Relative: yes

#Digilent WaveForms Network Analyzer - Bode
#Device Name: Discovery2
#Serial Number: SN:210321A18885
#Date Time: 2021-12-02 11:30:20.134
#Start: 100 Hz
#Stop: 1.79e+06 Hz
#Steps: 151
#Wavegen: Wavegen1
#Amplification: 1 X
#Settle: 10 ms
#MinPeriods: 16 
#Channel: Channel 2
#Range: 60.4918 V
#Offset: -0.00337698 V
#Relative: yes



#Digilent WaveForms Oscilloscope Acquisition
#Device Name: Discovery2
#Serial Number: DEMO
#Date Time: 2021-12-02 11:32:32.970
#Sample rate: 1.5873e+06Hz
#Samples: 8192
#Trigger: Source: Channel 1 Type: Edge Condition: Rising Level: 0 V Hyst.: Auto HoldOff: 0 s
#Channel 1: Range: 1 V/div Offset: 100 mV Attenuation: 1 X
#Channel 2: Range: 1 V/div Offset: 9.7 V Attenuation: 1 X
#Wavegen Channel 1: Enabled
#Mode: Simple
#Type: Square
#Frequency: 1 kHz
#Amplitude: 500 mV
#Offset: 0 V
#Symmetry: 50 %
#Phase: 0 �



"""

df_ol = pd.read_csv(   './LB10_data/LB10_firstreading.csv')
df_cl = pd.read_csv(   './LB10_data/LB10_closedloop.csv')
df_step = pd.read_csv( './LB10_data/LB10_stepresponse.csv')

df_list = [
df_ol,
df_cl,
]

title_list = [
'df_ol',
'df_cl',
]

# plot df_step 
df_step['Time (s)'] = df_step['Time (s)'].astype(float)
df_step['Channel 1 (V)'] = df_step['Channel 1 (V)'].astype(float)
df_step['Channel 2 (V)'] = df_step['Channel 2 (V)'].astype(float)

df_step['Channel 2 roll'] = df_step['Channel 2 (V)'].rolling(window=78).mean()


plt.figure("step response")
plt.plot(
    df_step['Time (s)'],  df_step['Channel 2 (V)'], 
    df_step['Time (s)'], df_step['Channel 1 (V)'], 
    df_step['Time (s)'], df_step['Channel 2 roll'], 
)
plt.legend(
    ['Measured Output',
    'Measured Input',
    'Measured Output Roll',],    
    loc='best')
# plt.xscale("log")
plt.title('Step Response')
plt.grid(True, which="both")
plt.xlabel('Time (s)')
plt.ylabel('Magnitude (dB)')
plt.savefig(f'./figs_lb10/step.png')

# waveforms data handling
for i,df in enumerate(df_list):
    df['Frequency (Hz)'] = df['Frequency (Hz)'].astype(float)
    # df['Channel 1 Magnitude (dB)'] = df['Channel 1 Magnitude (dB)'].astype(float)
    df['Channel 2 Magnitude (dB)'] = df['Channel 2 Magnitude (dB)'].astype(float)
    df['Channel 2 Phase (*)'] = df['Channel 2 Phase (*)'].astype(float)



# # CH2 Magnitude 
plt.figure("magnitude")
plt.plot(
    df_cl['Frequency (Hz)'],  df_cl['Channel 2 Magnitude (dB)'], 
    df_ol['Frequency (Hz)'], df_ol['Channel 2 Magnitude (dB)'], 
)
plt.legend(
    ['closed loop',
    'open loop',],    
    loc='best')
plt.xscale("log")
plt.title('Magnitude')
plt.grid(True, which="both")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.savefig(f'./figs_lb10/mag.png')

plt.figure("Phases")
# # CH2 Phase  
plt.plot(
    df_cl['Frequency (Hz)'],   df_cl['Channel 2 Phase (*)'], 
    df_ol['Frequency (Hz)'], df_ol['Channel 2 Phase (*)'], 
)
plt.legend(
    ['closed loop',
    'open loop',],    
    loc='best')
plt.title('Channel 2 Phase')
plt.xscale("log")
plt.grid(True, which="both")
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.savefig(f'./figs_lb10/phase.png')
plt.show()

plt.show()
