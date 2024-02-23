# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc("pdf", fonttype=42)
rc("font", size=20)
rc("axes", titlesize=25)
rc("legend", fontsize=10)
# Scientific color maps
from cmcrameri import cm
from os.path import exists
from os import mkdir
from pathlib import Path

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"

# Model names
models = [
          '5q_fixed_CERI_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed292846_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed292846_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
          '5q_fixed_CERI_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
         ]

labels = [
          'NS-1',
          'NS-2',
          'NS-3',
          'NS-4',
          'NS-5',
          'NS-6',
          'NS-7',
          'NS-8',
          'NS-9',
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
              'dashed',
              'solid']


# File name
tail = r"/topography."

# Create file paths
paths = [base+m for m in models]

max_topo = 0.

for m in models:
    counter = 0
    path = base + m
    output_name = m + '_'
    output_title = m
    if Path(path).exists():
       print ('Found dir') 
    for f in sorted(Path(path).glob('*topography*')):
        print(f"{f.name}\n")
        filename = path + "/" + f.name

        # Read in the topography of the current timestep. The file contains columns x, y, topo, of which we only need x, topo.
        # The correct columns are selected with usecols.
        x,topo = np.genfromtxt(filename, comments='#', usecols=(0,2), delimiter=' ', unpack=True)

        max_topo = max(max_topo,topo.max())

        # Plot the topography in km in 
        # categorical batlow colors.
        # And print the max topo in m.
        if (counter%10 == 0): 
            plt.plot(x/1000,topo/1000,label=str(0.5*counter)+" My",color=cmap(counter/50),linestyle='solid',marker='')
            max_topo = topo.max()
            plt.text(500,2.5-counter*0.03,f'Max {max_topo:.2f} m', color=cmap(counter/50), fontsize=8)
#        else:
#            plt.plot(x/1000,topo/1000,label=None,color=cmap(counter/50),linestyle='solid')
        counter += 1

    # Draw initial craton contour
    #plt.axvline(x=400, color='black', linestyle='dotted')

    # Draw sealevel at -200
    plt.axhline(y=-0.2, color='blue', linestyle='dashed')

    # Labelling of plot
    plt.xlabel("X [km]",weight="bold")
    plt.ylabel(r"Topography [km]",weight="bold")
    # Title 
    #plt.title(output_title)
    plt.grid(axis='x',color='0.95')
    plt.grid(axis='y',color='0.95')

    # Ranges of the axes
    plt.xlim(0,700) # km 
    plt.ylim(-5,4) # km
    plt.legend(ncol=1,loc="lower right")
    #plt.xticks([0,50,100,150,200,210])
    #plt.yticks([0,50,100,150,200,210])

    plt.tight_layout()

    # Make sure locally the corresponding folder exists
    if not Path(m).exists():
      mkdir(m)

    # Name the png according to the plotted field
    field='Topography'
    plt.savefig(m + '/' + output_name + '_CERI_' + str(field) + '.png', dpi=300)    
    print ('Produced:', m + '/' + output_name + '_CERI_' + str(field) + '.png')
    plt.clf()

print ("Maximum topography:", max_topo)
