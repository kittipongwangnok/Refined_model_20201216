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
InputFile_1 = "data_dpleo_20150318_run031kg5.txt"
Data_1   = np.genfromtxt(InputFile_1)

InputFile_2 = "output_dpleo_20150318_run031kg5.txt"
Data_2   = np.genfromtxt(InputFile_2)

InputFile_3 = "residual_dpleo_20150318_run031kg5.txt"
Data_3   = np.genfromtxt(InputFile_3)
#Read data ---#2
InputFile_4 = "data_dpleo_20161225_run024kg5.txt"
Data_4   = np.genfromtxt(InputFile_4)

InputFile_5 = "output_dpleo_20161225_run024kg5.txt"
Data_5   = np.genfromtxt(InputFile_5)

InputFile_6 = "residual_dpleo_20161225_run024kg5.txt"
Data_6   = np.genfromtxt(InputFile_6)
#Read data ---#3
InputFile_7 = "data_dpleo_20161225_run025kg5.txt"
Data_7   = np.genfromtxt(InputFile_7)

InputFile_8 = "output_dpleo_20161225_run025kg5.txt"
Data_8   = np.genfromtxt(InputFile_8)

InputFile_9 = "residual_dpleo_20161225_run025kg5.txt"
Data_9   = np.genfromtxt(InputFile_9)
#Read data ---#4
InputFile_10 = "data_dpleo_20170217_run033kg5.txt"
Data_10   = np.genfromtxt(InputFile_10)

InputFile_11 = "output_dpleo_20170217_run033kg5.txt"
Data_11   = np.genfromtxt(InputFile_11)

InputFile_12 = "residual_dpleo_20170217_run033kg5.txt"
Data_12   = np.genfromtxt(InputFile_12)
#Read data ---#5
InputFile_13 = "data_dpleo_20170217_run047kg5.txt"
Data_13   = np.genfromtxt(InputFile_13)

InputFile_14 = "output_dpleo_20170217_run047kg5.txt"
Data_14   = np.genfromtxt(InputFile_14)

InputFile_15 = "residual_dpleo_20170217_run047kg5.txt"
Data_15   = np.genfromtxt(InputFile_15)
#Read data ---#6
InputFile_16 = "data_dpleo_20170316_run036kg5.txt"
Data_16   = np.genfromtxt(InputFile_16)

InputFile_17 = "output_dpleo_20170316_run036kg5.txt"
Data_17   = np.genfromtxt(InputFile_17)

InputFile_18 = "residual_dpleo_20170316_run036kg5.txt"
Data_18   = np.genfromtxt(InputFile_18)
#Read data ---#7
InputFile_19 = "data_dpleo_20180121_run076kg5.txt"
Data_19   = np.genfromtxt(InputFile_19)

InputFile_20 = "output_dpleo_20180121_run076kg5.txt"
Data_20   = np.genfromtxt(InputFile_20)

InputFile_21 = "residual_dpleo_20180121_run076kg5.txt"
Data_21   = np.genfromtxt(InputFile_21)
#Read data ---#8
InputFile_22 = "data_dpleo_20180322_run021kg5.txt"
Data_22   = np.genfromtxt(InputFile_22)

InputFile_23 = "output_dpleo_20180322_run021kg5.txt"
Data_23   = np.genfromtxt(InputFile_23)

InputFile_24 = "residual_dpleo_20180322_run021kg5.txt"
Data_24   = np.genfromtxt(InputFile_24)
#Read data ---#9
InputFile_25 = "data_dpleo_20190227_run039kg5.txt"
Data_25   = np.genfromtxt(InputFile_25)

InputFile_26 = "output_dpleo_20190227_run039kg5.txt"
Data_26   = np.genfromtxt(InputFile_26)

InputFile_27 = "residual_dpleo_20190227_run039kg5.txt"
Data_27   = np.genfromtxt(InputFile_27)
#Read data ---#10
InputFile_28 = "data_dpleo_20190406_run021kg5.txt"
Data_28   = np.genfromtxt(InputFile_28)

InputFile_29 = "output_dpleo_20190406_run021kg5.txt"
Data_29   = np.genfromtxt(InputFile_29)

InputFile_30 = "residual_dpleo_20190406_run021kg5.txt"
Data_30   = np.genfromtxt(InputFile_30)
#Read data ---#11
InputFile_31 = "data_dpleo_20200124_run017kg5.txt"
Data_31   = np.genfromtxt(InputFile_31)

InputFile_32 = "output_dpleo_20200124_run017kg5.txt"
Data_32   = np.genfromtxt(InputFile_32)

InputFile_33 = "residual_dpleo_20200124_run017kg5.txt"
Data_33   = np.genfromtxt(InputFile_33)
#Read data ---#12
InputFile_34 = "data_dpleo_20200131_run009kg5.txt"
Data_34   = np.genfromtxt(InputFile_34)

InputFile_35 = "output_dpleo_20200131_run009kg5.txt"
Data_35   = np.genfromtxt(InputFile_35)

InputFile_36 = "residual_dpleo_20200131_run009kg5.txt"
Data_36   = np.genfromtxt(InputFile_36)
#Read data ---#13
InputFile_37 = "data_dpleo_20200229_run030kg5.txt"
Data_37   = np.genfromtxt(InputFile_37)

InputFile_38 = "output_dpleo_20200229_run030kg5.txt"
Data_38   = np.genfromtxt(InputFile_38)

InputFile_39 = "residual_dpleo_20200229_run030kg5.txt"
Data_39   = np.genfromtxt(InputFile_39)
#Read data ---#14
InputFile_40 = "data_dpleo_20200322_run026kg5.txt"
Data_40   = np.genfromtxt(InputFile_40)

InputFile_41 = "output_dpleo_20200322_run026kg5.txt"
Data_41   = np.genfromtxt(InputFile_41)

InputFile_42 = "residual_dpleo_20200322_run026kg5.txt"
Data_42   = np.genfromtxt(InputFile_42)

#DP Leo parameters
t0_20150318_run031kg5 = 57099.83254
t0_20161225_run024kg5 = 57747.78623
t0_20161225_run025kg5 = 57747.848525
t0_20170217_run033kg5 = 57801.72660
t0_20170217_run047kg5 = 57801.91368
t0_20170316_run036kg5 = 57828.85440
t0_20180121_run076kg5 = 58139.921675
t0_20180322_run021kg5 = 58199.72640
t0_20190227_run039kg5 = 58541.91108
t0_20190406_run021kg5 = 58579.57908
t0_20200124_run017kg5 = 58872.80960
t0_20200131_run009kg5 = 58879.66915
t0_20200229_run030kg5 = 58908.79166
t0_20200322_run026kg5 = 58930.61890
Period = 0.06236286

#Input calculation
#Input calculation ---#1
Cycle_1 = (Data_1[:,0] - t0_20150318_run031kg5)/Period
Phase_1 = Cycle_1
Flux_1 = Data_1[:,2]
Flux_err_1 = Data_1[:,3]
#Input calculation ---#2
Cycle_4 = (Data_4[:,0] - t0_20161225_run024kg5)/Period
Phase_4 = Cycle_4
Flux_4 = Data_4[:,2]
Flux_err_4 = Data_4[:,3]
#Input calculation ---#3
Cycle_7 = (Data_7[:,0] - t0_20161225_run025kg5)/Period
Phase_7 = Cycle_7
Flux_7 = Data_7[:,2]
Flux_err_7 = Data_7[:,3]
#Input calculation ---#4
Cycle_10 = (Data_10[:,0] - t0_20170217_run033kg5)/Period
E_10 = np.round(Cycle_10[0])
Phase_10 = Cycle_10 - E_10
Flux_10 = Data_10[:,2]
Flux_err_10 = Data_10[:,3]
#Input calculation ---#5
Cycle_13 = (Data_13[:,0] - t0_20170217_run047kg5)/Period
#E_10 = np.round(Cycle_10[0])
Phase_13 = Cycle_13
Flux_13 = Data_13[:,2]
Flux_err_13 = Data_13[:,3]
#Input calculation ---#6
Cycle_16 = (Data_16[:,0] - t0_20170316_run036kg5)/Period
#E_10 = np.round(Cycle_10[0])
Phase_16 = Cycle_16
Flux_16 = Data_16[:,2]
Flux_err_16 = Data_16[:,3]
#Input calculation ---#7
Cycle_19 = (Data_19[:,0] - t0_20180121_run076kg5)/Period
#E_10 = np.round(Cycle_10[0])
Phase_19 = Cycle_19
Flux_19 = Data_19[:,2]
Flux_err_19 = Data_19[:,3]
#Input calculation ---#8
Cycle_22 = (Data_22[:,0] - t0_20180322_run021kg5)/Period
#E_10 = np.round(Cycle_10[0])
Phase_22 = Cycle_22
Flux_22 = Data_22[:,2]
Flux_err_22 = Data_22[:,3]
#Input calculation ---#9
Cycle_25 = (Data_25[:,0] - t0_20190227_run039kg5)/Period
Phase_25 = Cycle_25
Flux_25 = Data_25[:,2]
Flux_err_25 = Data_25[:,3]
#Input calculation ---#10
Cycle_28 = (Data_28[:,0] - t0_20190406_run021kg5)/Period
Phase_28 = Cycle_28
Flux_28 = Data_28[:,2]
Flux_err_28 = Data_28[:,3]
#Input calculation ---#11
Cycle_31 = (Data_31[:,0] - t0_20200124_run017kg5)/Period
Phase_31 = Cycle_31
Flux_31 = Data_31[:,2]
Flux_err_31 = Data_31[:,3]
#Input calculation ---#12
Cycle_34 = (Data_34[:,0] - t0_20200131_run009kg5)/Period
Phase_34 = Cycle_34
Flux_34 = Data_34[:,2]
Flux_err_34 = Data_34[:,3]
#Input calculation ---#13
Cycle_37 = (Data_37[:,0] - t0_20200229_run030kg5)/Period
Phase_37 = Cycle_37
Flux_37 = Data_37[:,2]
Flux_err_37 = Data_37[:,3]
#Input calculation ---#14
Cycle_40 = (Data_40[:,0] - t0_20200322_run026kg5)/Period
Phase_40 = Cycle_40
Flux_40 = Data_40[:,2]
Flux_err_40 = Data_40[:,3]


#Output calculation
#Output calculation ---#1
Cycle_2 = (Data_2[:,0] - t0_20150318_run031kg5)/Period
Phase_2 = Cycle_2
Flux_2 = Data_2[:,2]
Flux_err_2 = Data_2[:,3]
#Output calculation ---#2
Cycle_5 = (Data_5[:,0] - t0_20161225_run024kg5)/Period
Phase_5 = Cycle_5
Flux_5 = Data_5[:,2]
Flux_err_5 = Data_5[:,3]
#Output calculation ---#3
Cycle_8 = (Data_8[:,0] - t0_20161225_run025kg5)/Period
Phase_8 = Cycle_8
Flux_8 = Data_8[:,2]
Flux_err_8 = Data_8[:,3]
#Output calculation ---#4
Cycle_11 = (Data_11[:,0] - t0_20170217_run033kg5)/Period
E_11 = np.round(Cycle_11[0])
Phase_11 = Cycle_11 - E_11
Flux_11 = Data_11[:,2]
Flux_err_11 = Data_11[:,3]
#Output calculation ---#5
Cycle_14 = (Data_14[:,0] - t0_20170217_run047kg5)/Period
#E_11 = np.round(Cycle_11[0])
Phase_14 = Cycle_14
Flux_14 = Data_14[:,2]
Flux_err_14 = Data_14[:,3]
#Output calculation ---#6
Cycle_17 = (Data_17[:,0] - t0_20170316_run036kg5)/Period
#E_11 = np.round(Cycle_11[0])
Phase_17 = Cycle_17
Flux_17 = Data_17[:,2]
Flux_err_17 = Data_17[:,3]
#Output calculation ---#7
Cycle_20 = (Data_20[:,0] - t0_20180121_run076kg5)/Period
#E_11 = np.round(Cycle_11[0])
Phase_20 = Cycle_20
Flux_20 = Data_20[:,2]
Flux_err_20 = Data_20[:,3]
#Output calculation ---#8
Cycle_23 = (Data_23[:,0] - t0_20180322_run021kg5)/Period
#E_11 = np.round(Cycle_11[0])
Phase_23 = Cycle_23
Flux_23 = Data_23[:,2]
Flux_err_23 = Data_23[:,3]
#Output calculation ---#9
Cycle_26 = (Data_26[:,0] - t0_20190227_run039kg5)/Period
Phase_26 = Cycle_26
Flux_26 = Data_26[:,2]
Flux_err_26 = Data_26[:,3]
#Output calculation ---#10
Cycle_29 = (Data_29[:,0] - t0_20190406_run021kg5)/Period
Phase_29 = Cycle_29
Flux_29 = Data_29[:,2]
Flux_err_29 = Data_29[:,3]
#Output calculation ---#11
Cycle_32 = (Data_32[:,0] - t0_20200124_run017kg5)/Period
Phase_32 = Cycle_32
Flux_32 = Data_32[:,2]
Flux_err_32 = Data_32[:,3]
#Input calculation ---#12
Cycle_35 = (Data_35[:,0] - t0_20200131_run009kg5)/Period
Phase_35 = Cycle_35
Flux_35 = Data_35[:,2]
Flux_err_35 = Data_35[:,3]
#Input calculation ---#13
Cycle_38 = (Data_38[:,0] - t0_20200229_run030kg5)/Period
Phase_38 = Cycle_38
Flux_38 = Data_38[:,2]
Flux_err_38 = Data_38[:,3]
#Input calculation ---#14
Cycle_41 = (Data_41[:,0] - t0_20200322_run026kg5)/Period
Phase_41 = Cycle_41
Flux_41 = Data_41[:,2]
Flux_err_41 = Data_41[:,3]

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
#Residual calculation ---#7
Res_1920 = Flux_19 - Flux_20
#Residual calculation ---#8
Res_2223 = Flux_22 - Flux_23
#Residual calculation ---#9
Res_2526 = Flux_25 - Flux_26
#Residual calculation ---#10
Res_2829 = Flux_28 - Flux_29
#Residual calculation ---#11
Res_3132 = Flux_31 - Flux_32
#Residual calculation ---#12
Res_3435 = Flux_34 - Flux_35
#Residual calculation ---#13
Res_3738 = Flux_37 - Flux_38
#Residual calculation ---#14
Res_4041 = Flux_40 - Flux_41

#Off set
off_set_1 = 0.05
off_set_2 = 0.10
off_set_3 = 0.15
off_set_4 = 0.20
off_set_5 = 0.25
off_set_6 = 0.30
off_set_7 = 0.35
off_set_8 = 0.40
off_set_9 = 0.45
off_set_10 = 0.50
off_set_11 = 0.55
off_set_12 = 0.60
off_set_13 = 0.65

fig, (ax0, ax1) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]}, sharex=True, sharey=False, figsize=(10, 10), tight_layout=True)
#plt.xlim(Phase_1[0], Phase_1[-1])
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

ax0.errorbar(Phase_19, Flux_19+off_set_6, yerr=Flux_err_19, fmt='o', markersize = 4, alpha = 0.25, color='cyan')
ax0.plot(Phase_20, Flux_20+off_set_6, 'b-')

ax0.errorbar(Phase_22, Flux_22+off_set_7, yerr=Flux_err_22, fmt='o', markersize = 4, alpha = 0.25, color='violet')
ax0.plot(Phase_23, Flux_23+off_set_7, 'b-')

ax0.errorbar(Phase_25, Flux_25+off_set_8, yerr=Flux_err_25, fmt='o', markersize = 4, alpha = 0.25, color='mistyrose')
ax0.plot(Phase_26, Flux_26+off_set_8, 'b-')

ax0.errorbar(Phase_28, Flux_28+off_set_9, yerr=Flux_err_28, fmt='o', markersize = 4, alpha = 0.25, color='lime')
ax0.plot(Phase_29, Flux_29+off_set_9, 'b-')

ax0.errorbar(Phase_31, Flux_31+off_set_10, yerr=Flux_err_31, fmt='o', markersize = 4, alpha = 0.25, color='salmon')
ax0.plot(Phase_32, Flux_32+off_set_10, 'b-')

ax0.errorbar(Phase_34, Flux_34+off_set_11, yerr=Flux_err_34, fmt='o', markersize = 4, alpha = 0.25, color='lightsteelblue')
ax0.plot(Phase_35, Flux_35+off_set_11, 'b-')

ax0.errorbar(Phase_37, Flux_37+off_set_12, yerr=Flux_err_37, fmt='o', markersize = 4, alpha = 0.25, color='bisque')
ax0.plot(Phase_38, Flux_38+off_set_12, 'b-')

ax0.errorbar(Phase_40, Flux_40+off_set_13, yerr=Flux_err_40, fmt='o', markersize = 4, alpha = 0.25, color='skyblue')
ax0.plot(Phase_41, Flux_41+off_set_13, 'b-')

ax0.text(0.4, 0.030, '20150318\_run031')
ax0.text(0.4, 0.090, '20161225\_run024')
ax0.text(0.4, 0.125, '20161225\_run025')
ax0.text(0.4, 0.165, '20170217\_run033')
ax0.text(0.4, 0.230, '20170217\_run047')
ax0.text(0.4, 0.270, '20170316\_run036')
ax0.text(0.4, 0.320, '20180121\_run076')
ax0.text(0.4, 0.370, '20180322\_run021')
ax0.text(0.4, 0.420, '20190227\_run039')
ax0.text(0.4, 0.470, '20190406\_run021')
ax0.text(0.4, 0.520, '20200124\_run017')
ax0.text(0.4, 0.570, '20200131\_run009')
ax0.text(0.4, 0.620, '20200229\_run030')
ax0.text(0.4, 0.670, '20200322\_run026')

#ax0.legend(loc="best")
ax0.set_ylabel('Relative flux')
ax0.set_ylim(-0.05, 0.7)

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

ax1.errorbar(Phase_19, Res_1920+off_set_6, yerr=Flux_err_19, fmt='o',markersize = 4, color='cyan', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_6, xmin=Phase_19[0], xmax=Phase_19[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_22, Res_2223+off_set_7, yerr=Flux_err_22, fmt='o',markersize = 4, color='violet', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_7, xmin=Phase_22[0], xmax=Phase_22[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_25, Res_2526+off_set_8, yerr=Flux_err_25, fmt='o',markersize = 4, color='mistyrose', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_8, xmin=Phase_25[0], xmax=Phase_25[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_28, Res_2829+off_set_9, yerr=Flux_err_28, fmt='o',markersize = 4, color='lime', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_9, xmin=Phase_28[0], xmax=Phase_28[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_31, Res_3132+off_set_10, yerr=Flux_err_31, fmt='o',markersize = 4, color='salmon', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_10, xmin=Phase_31[0], xmax=Phase_31[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_34, Res_3435+off_set_11, yerr=Flux_err_34, fmt='o',markersize = 4, color='lightsteelblue', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_11, xmin=Phase_34[0], xmax=Phase_34[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_37, Res_3738+off_set_12, yerr=Flux_err_37, fmt='o',markersize = 4, color='bisque', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_12, xmin=Phase_37[0], xmax=Phase_37[-1], colors='black', linestyles='-')

ax1.errorbar(Phase_40, Res_4041+off_set_13, yerr=Flux_err_40, fmt='o',markersize = 4, color='skyblue', alpha = 0.25, label = 'Res_data\_20200317\_run031g')
ax1.hlines(y=0+off_set_13, xmin=Phase_40[0], xmax=Phase_40[-1], colors='black', linestyles='-')

ax1.set_ylabel('Residual')
ax1.set_ylim(-0.05, 0.7)


fig.align_ylabels()
output_filename = os.path.splitext(__file__)[0] + '.png'
plt.savefig(output_filename, dpi=1000)
plt.show()

