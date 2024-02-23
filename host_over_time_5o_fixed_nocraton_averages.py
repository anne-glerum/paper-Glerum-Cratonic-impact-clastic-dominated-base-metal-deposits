# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
# Do not put 1e10 at the top of graph,
# but with the respective tick labels.
# TODO: nothing works to turn it off.
rc('axes.formatter', useoffset=False)
# Scientific color maps
from cmcrameri import cm
from os.path import exists
import io
import re
plt.rcParams["font.family"] = "Arial"
rc("xtick", labelsize= 12)
rc("font", size=12)
rc("axes", titlesize=15, labelsize=12)
#rc('axes', linewidth=3)
rc("legend", fontsize=8)

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT/"

# Model names
models = [
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
         ]

output_name = '5o_fixed_craton2000km_rain0.0001_Km210_Km70_Kf1e-5_vel10_'

n_models = len(models)
print ("Plotting " + str(n_models) + " models plus their average")

labels = [
          'W-1',
          'W-2',
          'W-3',
          'W-4',
          'W-5',
          'W-6',
          'W-7',
          'W-8',
          'W-9',
          'W-av.',
         ]

# Batlow
color1=[0.0051932, 0.098238, 0.34984]
color2=[0.063071, 0.24709, 0.37505]
color3=[0.10684, 0.34977, 0.38455]
color4=[0.23136, 0.4262, 0.33857]
color5=[0.40297, 0.48047, 0.24473]
color6=[0.60052, 0.5336, 0.17065]
color7=[0.81169, 0.57519, 0.25257]
color8=[0.96494, 0.62693, 0.46486]
color9=[0.99277, 0.70769, 0.71238]
color10=[0.98332, 0.79091, 0.95375]
colors = [
          color1, 
          color2, 
          color3, 
          color4, 
          color5, 
          color6, 
          color7, 
          color8, 
          color9,
          color10,
         ]
cmap = plt.cm.get_cmap(cm.batlow)

linestyles = [
              'solid', 
              'dashed',
              'dotted', 
              'solid', 
              'dotted', 
              'dashdot',
              'dashdot',
              'dashdot',
              'dashed',
              'dashed',
              'dashdot',
             ]
markers = [
           '','','','','','','','','',''
          ]
dmark = 200

# File name
tail = r"/statistics"

cm = 2.54  # centimeters in inches
fig = plt.figure(figsize=(10.5/cm,6.6/cm),dpi=300)

# Create file paths
paths = [base+m+tail for m in models]

mean_t = np.arange(0, 25e6, 2500)
average_host_area = [0.0 for t in mean_t]

counter = 0
max_host = -2e9
average_max_host = 0

for p in paths:
    print(p)
    # Read in the area of the current timestep. 
    # The correct columns are selected with usecols.
    # When no visu output file name is given, the respective line will have a lot of
    # placeholder spaces. We need to remove them before genfromtxt can deal with the
    # statistics file. 
    with open(p) as f:
        clean_lines = (re.sub('\s+',' ',line) for line in f)
        t,host_area = np.genfromtxt(clean_lines, comments='#', usecols=(1,63), delimiter=' ', unpack=True)

    # Interpolate to a predefined set of timesteps, as not all runs have the same number
    # of timesteps.
    interpolated_host_area = np.interp(mean_t, t, host_area)

    average_host_area += interpolated_host_area

    # Plot the area in km2 in 
    # categorical batlow colors.
    plt.plot(t/1e6,host_area/1e6,color=colors[counter],linestyle='solid',label=labels[counter],marker=markers[counter],markevery=dmark,fillstyle='none')

    # Compute the max host area over the 25 My and all runs
    max_host = max(host_area.max(),max_host)
    # Add the max host area of this run to the sum
    average_max_host += host_area.max()

    counter += 1

# The max host area at any point in time of all runs
print ("Max host area:", max_host/1e6, "km2")
# The average of the max host area of each run
print ("Average max host area:", average_max_host/n_models/1e6, "km2")
# The max of the average host area of each run
print ("Max average host area:", (average_host_area/n_models).max()/1e6, "km2")

# Plot the average host area over time (divide by nine to get the average)
plt.plot(mean_t/1e6,average_host_area/n_models/1e6,color=colors[counter],linestyle='solid',label=labels[counter],marker=markers[counter],markevery=dmark,fillstyle='none',linewidth=3)

# Labelling of plot
plt.xlabel("Time [My]",weight="bold")
plt.ylabel(r"Host area [km$\mathbf{^2}$]",weight="bold")
# Manually place legend in lower right corner. 
plt.legend(loc='upper left',ncol=2)
# Title 
#plt.title("Sediment area over time")
plt.grid(axis='x',color='0.95')
plt.grid(axis='y',color='0.95')

# Ranges of the axes
plt.xlim(-0.25,25.25) # My
plt.ylim(-30,300) # km2
ax = plt.gca()
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.ticklabel_format(axis='y',useOffset=False)
plt.xticks(np.arange(0,30,5))
#plt.yticks([0,50,100,150,200,210])

plt.tight_layout()

# Name the png according to the plotted field
# Change as needed
field='host_area_'
plt.savefig(output_name + '_CERI_' + str(field) + '.png')    
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
