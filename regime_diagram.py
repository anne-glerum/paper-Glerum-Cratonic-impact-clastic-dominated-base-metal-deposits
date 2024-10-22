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
from sys import exit
import io
import re
import pandas as pd
import seaborn as sns
plt.rcParams["font.family"] = "Arial"
rc("xtick", labelsize= 12)
rc("font", size=12)
rc("axes", titlesize=15, labelsize=12)
#rc('axes', linewidth=3)
rc("legend", fontsize=8)

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

# Model names
models = [
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
         ]

output_name = '5p_fixed_regime_'

to_plot = ['start_migration', 'max_OFM3']

labels = [
#          'NA-1',
          'NA-2',
          'NA-3',
          'NA-4',
#          'NA-5',
          'NA-6',
#          'NA-7',
          'NA-8',
          'NA-9',
          'NA-av.',
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
#          color1, 
          color2, 
          color3, 
          color4, 
#          color5, 
          color6, 
#          color7, 
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
tail = r"5p_fixed_CERI_craton_analysis.txt"

# Read the data file
dataframe = pd.read_csv(base+tail, sep=",")

# Check data
print ("Interpretation data file: ", dataframe.dtypes)
if not set(to_plot).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")
if not set(["max_OFM3","max_OFM2","max_OFM1","max_source"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# Create empty plot
sns.set_theme()
cm = 2.54  # centimeters in inches
fig, axs = plt.subplots(2,4) #,figsize=(6, 2),dpi=300)

# Plot requested columns
#dataframe.plot.scatter(x=to_plot[0],y=to_plot[1],alpha=0.5,s=dataframe["max_source"]*10,color=cmap(dataframe["max_OFM1"]/5))
sns.scatterplot(data=dataframe,x=to_plot[0],y=to_plot[1],size="max_source",sizes=(0,200),hue="max_OFM1",ax=axs[0,0],legend=False)
sns.scatterplot(data=dataframe,x=to_plot[1],y=to_plot[0],size="max_source",sizes=(0,200),hue="max_OFM1",ax=axs[1,0],legend=True)

# Ranges and labels of the axes
axs[0,0].set_title("Initial rift-craton distance: " + str(dataframe["initial_craton_distance"][0]) + " km", weight="bold")
#
#if to_plot[0] == 'initial_craton_distance':
#  plt.xlim(-1.5,151.5) # km
#  plt.xlabel("Initial craton-rift distance [km]",weight="bold")
##if to_plot[0] == 'initial_fault_geometry':
##  plt.xlim(-1.5,151.5) # km
#elif to_plot[0] == 'start_migration':
#  plt.xlim(-0.25,25.25) # My
#  plt.xlabel("Start rift migration [My]",weight="bold")
##if to_plot[0] == 'narrow_margin':
#elif to_plot[0] == 'start_border_fault':
#  plt.xlim(-0.25,25.25) # My
#  plt.xlabel("Start source basin border fault(s) [My]",weight="bold")
#elif to_plot[0] == 'max_source_basins':
#  plt.xlim(-0.1,10.1) # -
#  plt.xlabel("Max. nr of source basins [-]",weight="bold")
#elif to_plot[0] == 'max_source_host_basins':
#  plt.xlim(-0.1,10.1) # -
#  plt.xlabel("Max. nr of source+host basins [-]",weight="bold")
#elif to_plot[0] == 'max_OFM3':
#  plt.xlim(-0.05,5.05) # -
#  plt.xlabel("Max. nr of OFM3 [-]",weight="bold")
#elif to_plot[0] == 'max_OFM2':
#  plt.xlim(-0.05,5.05) # -
#  plt.xlabel("Max. nr of OFM2 [-]",weight="bold")
#elif to_plot[0] == 'max_OMF1':
#  plt.xlim(-0.05,5.05) # -
#  plt.xlabel("Max. nr of OFM1 [-]",weight="bold")
#elif to_plot[0] == 'end_migration':
#  plt.xlim(-0.25,25.25) # My
#  plt.xlabel("End rift migration [My]",weight="bold")
#
#if to_plot[1] == 'initial_craton_distance':
#  plt.ylim(-1.5,151.5) # km
#  plt.ylabel("Initial craton-rift distance [km]",weight="bold")
##if to_plot[1] == 'initial_fault_geometry':
##  plt.ylim(-1.5,151.5) # km
#elif to_plot[1] == 'start_migration':
#  plt.ylim(-0.25,25.25) # My
#  plt.ylabel("Start rift migration [My]",weight="bold")
##if to_plot[1] == 'narrow_margin':
#elif to_plot[1] == 'start_border_fault':
#  plt.ylim(-0.25,25.25) # My
#  plt.ylabel("Start source basin border fault(s) [My]",weight="bold")
#elif to_plot[1] == 'max_source_basins':
#  plt.ylim(-0.1,10.1) # -
#  plt.ylabel("Max. nr of source basins [-]",weight="bold")
#elif to_plot[1] == 'max_source_host_basins':
#  plt.ylim(-0.1,10.1) # -
#  plt.ylabel("Max. nr of source+host basins [-]",weight="bold")
#elif to_plot[1] == 'max_OFM3':
#  plt.ylim(-0.05,5.05) # -
#  plt.ylabel("Max. nr of OFM3 [-]",weight="bold")
#elif to_plot[1] == 'max_OFM2':
#  plt.ylim(-0.05,5.05) # -
#  plt.ylabel("Max. nr of OFM2 [-]",weight="bold")
#elif to_plot[1] == 'max_OMF1':
#  plt.ylim(-0.05,5.05) # -
#  plt.ylabel("Max. nr of OFM1 [-]",weight="bold")
#elif to_plot[1] == 'end_migration':
#  plt.ylim(-0.25,25.25) # My
#  plt.ylabel("End rift migration [My]",weight="bold")

# Axis labels
#ax = plt.gca()
#ax.get_yaxis().get_major_formatter().set_useOffset(False)
#plt.ticklabel_format(axis='y',useOffset=False)
#plt.xticks(np.arange(0,30,5))
##plt.yticks([0,50,100,150,200,210])
plt.show()

## Labelling of plot
## Manually place legend in lower right corner. 
#plt.legend(loc='upper left',ncol=3)
## Title 
#plt.grid(axis='x',color='0.95')
#plt.grid(axis='y',color='0.95')
#
#
#plt.tight_layout()
#
## Name the png according to the plotted field
## Change as needed
#field='source_area_'
#plt.savefig(output_name + '_CERI_' + str(field) + '.png')    
#print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
