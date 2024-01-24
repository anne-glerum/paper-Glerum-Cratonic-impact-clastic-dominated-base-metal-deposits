# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
# Scientific color maps
from cmcrameri import cm
from os.path import exists
plt.rcParams["font.family"] = "Arial"
rc("xtick", labelsize= 12)
rc("font", size=12)
rc("axes", titlesize=15, labelsize=12)
rc("legend", fontsize=5)

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"

# Model names
models = [
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_craton450km_notopopert_RBIPS5kmnosubres_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel5_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_notopopert_RBIPS5kmnosubres_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
         ]

output_name = '5p_fixed_craton500km_'
x_craton_edge = 500
output_title = models[0]

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
tail = r"/topography."

# Create file paths
paths = [base+m+tail for m in models]
timesteps = [289,575,861,1147,1432,2861,4289,5718,7147]
print (timesteps)
dtrange=0

cm = 2.54  # centimeters in inches
fig = plt.figure(figsize=(10.5/cm,6.6/cm),dpi=300)

counter = 0 
for t in timesteps:
  counter = 0
  for p in paths:
    if t == 0:
      filename = p+"00000"
    else:
      filename = p+str(t+dtrange).rjust(5,'0')
    file_exists = exists(filename)
    if file_exists:
      print(filename, "exists")
    else:
      print(filename, "does not exist")

    if file_exists:
       # Read in the topography of the current timestep. The file contains columns x, y, topo, of which we only need x, topo.
       # The correct columns are selected with usecols.
       x,topo = np.genfromtxt(filename, comments='#', usecols=(0,2), delimiter=' ', unpack=True)

       # Plot the topography in km in 
       # categorical batlow colors.
       plt.plot(x/1000,topo/1000,label=labels[counter],color=colors[counter],linestyle='solid')

    counter += 1
    # Draw initial craton contour
  plt.axvline(x=x_craton_edge, color='black', linestyle='dotted')

  # Draw sealevel at -200
  plt.axhline(y=-0.2, color='blue', linestyle='dashed')

  # Labelling of plot
  plt.xlabel("X [km]")
  plt.ylabel(r"Topography [km]")
  # Title 
  #plt.title("Topography over time " + str(t) + output_title)
  plt.title("Topography at " + str(((t-5)*3500+6200)/1e6) + " My")
  plt.grid(axis='x',color='0.95')
  plt.grid(axis='y',color='0.95')
  
  # Ranges of the axes
  #plt.xlim(-500,1500) # km 
  plt.xlim(0,700) # km 
  plt.ylim(-5.5,2.5) # km
  plt.legend(ncol=2,loc="lower left")
  plt.xticks([0,100,200,300,400,500,600,700])
  #plt.yticks([0,50,100,150,200,210])
  
  plt.tight_layout()
  
  # Name the png according to the plotted field
  # Change as needed
  field='topography'
  plt.savefig(output_name + '_CERI_' + str(field) + '_' + str(((t-5)*3500+6200)/1e6) + 'My.png')    
  plt.clf()
  print ("Output in: ", output_name + '_CERI_' + str(field) + '_' + str(((t-5)*3500+6200)/1e6) + 'My.png')
