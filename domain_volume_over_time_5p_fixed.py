# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
# Scientific color maps
from cmcrameri import cm
from os.path import exists
import io
import re

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"
base = r"./"

# Model names
models = [
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_flatsurfacet0_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_flatsurfacet0_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
         ]

#output_name = '5p_fixed_craton400km_rain0.0001_Km210_Km70_Kf1e-5_vel10_'
output_name = '5p_fixed_flatsurfacet0_craton500km_rain0.0001_Km210_Km70_Kf1e-5_vel10_'

n_models = len(models)
print ("Plotting " + str(n_models) + " models plus their average")

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
         ]
cmap = plt.cm.get_cmap(cm.batlow)

linestyles = [
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'dashed',
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'solid', 
              'dashed',
              'dotted', 
              'dashdot',
              'dashed',
              'dotted', 
              'dashdot',
              'solid']

labels = [
          'NA-1',
          'NA-2',
          'NA-3',
          'NA-4',
          'NA-5',
          'NA-6',
          'NA-7',
          'NA-8',
          'NA-9',
          'NA-av.',
         ]

# File name
tail = r"/statistics"
tail = r"/statistics_domain_volume"

# Create file paths
paths = [base+m+tail for m in models]

counter = 0

for p in paths:
    print(p)
    # Read in the volume of the current timestep. 
    # The correct columns are selected with usecols.
    # When no visu output file name is given, the respective line will have a lot of
    # placeholder spaces. We need to remove them before genfromtxt can deal with the
    # statistics file. 
    with open(p) as f:
        clean_lines = (re.sub('\s+',' ',line) for line in f)
        #t,volume = np.genfromtxt(clean_lines, comments='#', usecols=(1,61), delimiter=' ', unpack=True)
        t,volume = np.genfromtxt(clean_lines, comments='#', usecols=(0,1), delimiter=' ', unpack=True)

    # Plot the volume in m2 in 
    # categorical batlow colors.
    plt.plot(t/1e6,volume/(700000*300000),color=colors[counter],linestyle='solid',label=labels[counter])
    counter += 1

# Labelling of plot
plt.xlabel("Time [My]")
plt.ylabel(r"Normalized volume [-]")
# Manually place legend in lower right corner. 
plt.legend(loc='center right')
# Title 
plt.title("Model domain volume over time")
plt.grid(axis='x',color='0.95')
plt.grid(axis='y',color='0.95')

# Ranges of the axes
#plt.xlim(0,6.5) # Myk
#plt.ylim(6e11,6.005e11) # m2
#plt.xticks([0,50,100,150,200,210])
#plt.yticks([0,50,100,150,200,210])

plt.tight_layout()

# Name the png according to the plotted field
# Change as needed
field='domain_volume'
plt.savefig(output_name + '_CERI_' + str(field) + '.png')    
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
