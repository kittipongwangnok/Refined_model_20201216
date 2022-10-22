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
InputFile_1 = "data_dpleo_20170314_run039r.txt"
Data_1   = np.genfromtxt(InputFile_1)

InputFile_2 = "output_dpleo_20170314_run039r.txt"
Data_2   = np.genfromtxt(InputFile_2)

InputFile_3 = "residual_dpleo_20170314_run039r.txt"
Data_3   = np.genfromtxt(InputFile_3)
#Read data ---#2
InputFile_4 = "data_dpleo_20200121_run057r.txt"
Data_4   = np.genfromtxt(InputFile_4)

InputFile_5 = "output_dpleo_20200121_run057r.txt"
Data_5   = np.genfromtxt(InputFile_5)

InputFile_6 = "residual_dpleo_20200121_run057r.txt"
Data_6   = np.genfromtxt(InputFile_6)
#Read data ---#3
InputFile_7 = "data_dpleo_20200122_run030r.txt"
Data_7   = np.genfromtxt(InputFile_7)

InputFile_8 = "output_dpleo_20200122_run030r.txt"
Data_8   = np.genfromtxt(InputFile_8)

InputFile_9 = "residual_dpleo_20200122_run030r.txt"
Data_9   = np.genfromtxt(InputFile_9)


#DP Leo parameters
t0_20170314_run039r = 57826.796430
t0_20200121_run057r = 58869.878700
t0_20200122_run030r = 58870.751725
Period = 0.06236286

#Input calculation
#Input calculation ---#1
Cycle_1 = (Data_1[:,0] - t0_20170314_run039r)/Period
Phase_1 = Cycle_1
Flux_1 = Data_1[:,2]
Flux_err_1 = Data_1[:,3]
#Input calculation ---#2
Cycle_4 = (Data_4[:,0] - t0_20200121_run057r)/Period
Phase_4 = Cycle_4
Flux_4 = Data_4[:,2]
Flux_err_4 = Data_4[:,3]
#Input calculation ---#3
Cycle_7 = (Data_7[:,0] - t0_20200122_run030r)/Period
Phase_7 = Cycle_7
Flux_7 = Data_7[:,2]
Flux_err_7 = Data_7[:,3]


#Output calculation
#Output calculation ---#1
Cycle_2 = (Data_2[:,0] - t0_20170314_run039r)/Period
Phase_2 = Cycle_2
Flux_2 = Data_2[:,2]
Flux_err_2 = Data_2[:,3]
#Output calculation ---#2
Cycle_5 = (Data_5[:,0] - t0_20200121_run057r)/Period
Phase_5 = Cycle_5
Flux_5 = Data_5[:,2]
Flux_err_5 = Data_5[:,3]
#Output calculation ---#3
Cycle_8 = (Data_8[:,0] - t0_20200122_run030r)/Period
Phase_8 = Cycle_8
Flux_8 = Data_8[:,2]
Flux_err_8 = Data_8[:,3]


#Residual calculation
#Residual calculation ---#1
Res_12 = Flux_1 - Flux_2
#Residual calculation ---#2
Res_45 = Flux_4 - Flux_5
#Residual calculation ---#3
Res_78 = Flux_7 - Flux_8


#Off set
off_set_1 = 0.025
off_set_2 = 0.050
#off_set_3 = 0.075

fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]}, sharex=True, sharey=False, figsize=(10, 6), tight_layout=True)
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



ax0.text(0.12, 0.005, '20170314\_run039')
ax0.text(0.12, 0.052, '20200121\_run057')
ax0.text(0.12, 0.070, '20200122\_run030')



#ax0.legend(loc="best")
ax0.set_ylabel('Relative flux')

ax1.errorbar(Phase_1, Res_12, yerr=Flux_err_1, fmt='o',markersize = 4, color='red', alpha = 0.25, label = 'Res_data\_20170314\_run039g')
ax1.hlines(y=0, xmin=Phase_1[0], xmax=Phase_1[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_4, Res_45+off_set_1, yerr=Flux_err_4, fmt='o',markersize = 4, color='green', alpha = 0.25, label = 'Res_data\_20200102\_run008g')
ax1.hlines(y=0+off_set_1, xmin=Phase_4[0], xmax=Phase_4[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_7, Res_78+off_set_2, yerr=Flux_err_7, fmt='o',markersize = 4, color='orange', alpha = 0.25, label = 'Res_data\_20200121\_run036g')
ax1.hlines(y=0+off_set_2, xmin=Phase_7[0], xmax=Phase_7[-1], colors='black', linestyles='-')


ax1.set_ylabel('Residual')


fig.align_ylabels()
output_filename = os.path.splitext(__file__)[0] + '.png'
plt.savefig(output_filename, dpi=1000)
plt.show()

