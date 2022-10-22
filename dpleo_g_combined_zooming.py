#PhD reseach 2020
#Kittipong Wangnok, D6010218
#School of Physics, Institute of Science, Suranaree University of Technology

#Import all module
import sys
import os
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean
np.seterr(divide='ignore', invalid='ignore')

#Latex font
import matplotlib as mpl
from matplotlib import rc
plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=16)

#################################################################################
'''
1. Input file: lcurve_dpleo_data
'''
#################################################################################
#Read data ---#1
InputFile_1 = "data_dpleo_20150319_run032g.txt"
Data_1   = np.genfromtxt(InputFile_1)

InputFile_2 = "output_dpleo_20150319_run032g.txt"
Data_2   = np.genfromtxt(InputFile_2)

InputFile_3 = "residual_dpleo_20150319_run032g.txt"
Data_3   = np.genfromtxt(InputFile_3)
#Read data ---#2
InputFile_4 = "data_dpleo_20200102_run008g.txt"
Data_4   = np.genfromtxt(InputFile_4)

InputFile_5 = "output_dpleo_20200102_run008g.txt"
Data_5   = np.genfromtxt(InputFile_5)

InputFile_6 = "residual_dpleo_20200102_run008g.txt"
Data_6   = np.genfromtxt(InputFile_6)
#Read data ---#3
InputFile_7 = "data_dpleo_20200121_run036g.txt"
Data_7   = np.genfromtxt(InputFile_7)

InputFile_8 = "output_dpleo_20200121_run036g.txt"
Data_8   = np.genfromtxt(InputFile_8)

InputFile_9 = "residual_dpleo_20200121_run036g.txt"
Data_9   = np.genfromtxt(InputFile_9)
#Read data ---#4
InputFile_10 = "data_dpleo_20200122_run028g.txt"
Data_10   = np.genfromtxt(InputFile_10)

InputFile_11 = "output_dpleo_20200122_run028g.txt"
Data_11   = np.genfromtxt(InputFile_11)

InputFile_12 = "residual_dpleo_20200122_run028g.txt"
Data_12   = np.genfromtxt(InputFile_12)
#Read data ---#5
InputFile_13 = "data_dpleo_20200124_run022g.txt"
Data_13   = np.genfromtxt(InputFile_13)

InputFile_14 = "output_dpleo_20200124_run022g.txt"
Data_14   = np.genfromtxt(InputFile_14)

InputFile_15 = "residual_dpleo_20200124_run022g.txt"
Data_15   = np.genfromtxt(InputFile_15)
#Read data ---#6
InputFile_16 = "data_dpleo_20200317_run031g.txt"
Data_16   = np.genfromtxt(InputFile_16)

InputFile_17 = "output_dpleo_20200317_run031g.txt"
Data_17   = np.genfromtxt(InputFile_17)

InputFile_18 = "residual_dpleo_20200317_run031g.txt"
Data_18   = np.genfromtxt(InputFile_18)

#DP Leo parameters
t0_20150319_run032g = 57100.64330
t0_20200102_run008g = 58850.79715
t0_20200121_run036g = 58869.75395
t0_20200122_run028g = 58869.75395
t0_20200124_run022g = 58872.93440
t0_20200317_run031g = 58925.62975
Period = 0.06236286

#Input calculation
#Input calculation ---#1
Cycle_1 = (Data_1[:,0] - t0_20150319_run032g)/Period
Phase_1 = Cycle_1
Flux_1 = Data_1[:,2]
Flux_err_1 = Data_1[:,3]
#Input calculation ---#2
Cycle_4 = (Data_4[:,0] - t0_20200102_run008g)/Period
Phase_4 = Cycle_4
Flux_4 = Data_4[:,2]
Flux_err_4 = Data_4[:,3]
#Input calculation ---#3
Cycle_7 = (Data_7[:,0] - t0_20200121_run036g)/Period
Phase_7 = Cycle_7
Flux_7 = Data_7[:,2]
Flux_err_7 = Data_7[:,3]
#Input calculation ---#4
Cycle_10 = (Data_10[:,0] - t0_20200122_run028g)/Period
E_10 = np.round(Cycle_10[0])
Phase_10 = Cycle_10 - E_10
Flux_10 = Data_10[:,2]
Flux_err_10 = Data_10[:,3]
#Input calculation ---#5
Cycle_13 = (Data_13[:,0] - t0_20200124_run022g)/Period
#E_10 = np.round(Cycle_10[0])
Phase_13 = Cycle_13
Flux_13 = Data_13[:,2]
Flux_err_13 = Data_13[:,3]
#Input calculation ---#6
Cycle_16 = (Data_16[:,0] - t0_20200317_run031g)/Period
#E_10 = np.round(Cycle_10[0])
Phase_16 = Cycle_16
Flux_16 = Data_16[:,2]
Flux_err_16 = Data_16[:,3]

#Output calculation
#Output calculation ---#1
Cycle_2 = (Data_2[:,0] - t0_20150319_run032g)/Period
Phase_2 = Cycle_2
Flux_2 = Data_2[:,2]
Flux_err_2 = Data_2[:,3]
#Output calculation ---#2
Cycle_5 = (Data_5[:,0] - t0_20200102_run008g)/Period
Phase_5 = Cycle_5
Flux_5 = Data_5[:,2]
Flux_err_5 = Data_5[:,3]
#Output calculation ---#3
Cycle_8 = (Data_8[:,0] - t0_20200121_run036g)/Period
Phase_8 = Cycle_8
Flux_8 = Data_8[:,2]
Flux_err_8 = Data_8[:,3]
#Output calculation ---#4
Cycle_11 = (Data_11[:,0] - t0_20200122_run028g)/Period
E_11 = np.round(Cycle_11[0])
Phase_11 = Cycle_11 - E_11
Flux_11 = Data_11[:,2]
Flux_err_11 = Data_11[:,3]
#Output calculation ---#5
Cycle_14 = (Data_14[:,0] - t0_20200124_run022g)/Period
#E_11 = np.round(Cycle_11[0])
Phase_14 = Cycle_14
Flux_14 = Data_14[:,2]
Flux_err_14 = Data_14[:,3]
#Output calculation ---#6
Cycle_17 = (Data_17[:,0] - t0_20200317_run031g)/Period
#E_11 = np.round(Cycle_11[0])
Phase_17 = Cycle_17
Flux_17 = Data_17[:,2]
Flux_err_17 = Data_17[:,3]

#Residual calculation
#Residual calculation ---#1
Res_12 = Flux_1 - Flux_2
#Residual calculation ---#2
Res_45 = Flux_4 - Flux_5
#Residual calculation ---#3
Res_78 = Flux_7 - Flux_8
#Residual calculation ---#4
Res_1011 = Flux_10 - Flux_11
#Residual calculation ---#5
Res_1314 = Flux_13 - Flux_14
#Residual calculation ---#6
Res_1617 = Flux_16 - Flux_17

#Off set
off_set_1 = 0.025
off_set_2 = 0.050
off_set_3 = 0.075
off_set_4 = 0.100
off_set_5 = 0.125

fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1.25]}, sharex=True, sharey=False, figsize=(10, 6), tight_layout=True)
plt.xlim(-0.2, 0.2)
plt.xlabel('Orbital phase')

ax0.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax1.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')


ax0.errorbar(Phase_1, Flux_1, yerr=Flux_err_1, fmt='o', markersize = 4, alpha = 0.25, color='red')
ax0.plot(Phase_2, Flux_2, 'b-')

ax0.errorbar(Phase_4, Flux_4+off_set_1, yerr=Flux_err_4, fmt='o', markersize = 4, alpha = 0.25, color='green')
ax0.plot(Phase_5, Flux_5+off_set_1, 'b-')

ax0.errorbar(Phase_7, Flux_7+off_set_2, yerr=Flux_err_7, fmt='o', markersize = 4, alpha = 0.25, color='orange')
ax0.plot(Phase_8, Flux_8+off_set_2, 'b-')

ax0.errorbar(Phase_10, Flux_10+off_set_3, yerr=Flux_err_10, fmt='o', markersize = 4, alpha = 0.25, color='pink')
ax0.plot(Phase_11, Flux_11+off_set_3, 'b-')

ax0.errorbar(Phase_13, Flux_13+off_set_4, yerr=Flux_err_13, fmt='o', markersize = 4, alpha = 0.25, color='grey')
ax0.plot(Phase_14, Flux_14+off_set_4, 'b-')

ax0.errorbar(Phase_16, Flux_16+off_set_5, yerr=Flux_err_16, fmt='o', markersize = 4, alpha = 0.25, color='yellow')
ax0.plot(Phase_17, Flux_17+off_set_5, 'b-')

ax0.text(0.12, 0.040, '20150319\_run032')
ax0.text(0.12, 0.060, '20200102\_run008')
ax0.text(0.12, 0.085, '20200121\_run036')
ax0.text(0.12, 0.110, '20200122\_run028')
ax0.text(0.12, 0.140, '20200124\_run022')
ax0.text(0.12, 0.160, '20200317\_run031')


#ax0.legend(loc="best")
ax0.set_ylabel('Relative flux')

ax1.errorbar(Phase_1, Res_12, yerr=Flux_err_1, fmt='o',markersize = 4, color='red', alpha = 0.25, label = 'Res_data\_20150319\_run032g')
ax1.hlines(y=0, xmin=Phase_1[0], xmax=Phase_1[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_4, Res_45+off_set_1, yerr=Flux_err_4, fmt='o',markersize = 4, color='green', alpha = 0.25, label = 'Res_data\_20200102\_run008g')
ax1.hlines(y=0+off_set_1, xmin=Phase_4[0], xmax=Phase_4[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_7, Res_78+off_set_2, yerr=Flux_err_7, fmt='o',markersize = 4, color='orange', alpha = 0.25, label = 'Res_data\_20200121\_run036g')
ax1.hlines(y=0+off_set_2, xmin=Phase_7[0], xmax=Phase_7[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_10, Res_1011+off_set_3, yerr=Flux_err_10, fmt='o',markersize = 4, color='pink', alpha = 0.25, label = 'Res_data\_20200122\_run028g')
ax1.hlines(y=0+off_set_3, xmin=Phase_10[0], xmax=Phase_10[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_13, Res_1314+off_set_4, yerr=Flux_err_13, fmt='o',markersize = 4, color='grey', alpha = 0.25, label = 'Res_data\_20200124\_run022g')
ax1.hlines(y=0+off_set_4, xmin=Phase_13[0], xmax=Phase_13[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_16, Res_1617+off_set_5, yerr=Flux_err_16, fmt='o',markersize = 4, color='yellow', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_5, xmin=Phase_16[0], xmax=Phase_16[-1], colors='black', linestyles='-')


ax1.set_ylabel('Residual')


fig.align_ylabels()
output_filename = os.path.splitext(__file__)[0] + '.png'
plt.savefig(output_filename, dpi=1000)
plt.show()

