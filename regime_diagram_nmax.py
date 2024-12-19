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
from sys import exit
import io
import re
import pandas as pd
import seaborn as sns
plt.rcParams["font.family"] = "Arial"
rc("xtick", labelsize= 12)
rc("font", size=12)
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

output_name = '5p_fixed_regime_diagram_'

to_plot = ['start_migration', 'n_OFM3_max']

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
# test file
tail = r"5p_fixed_CERI_craton_analysis.txt"
# real file
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"

# Read the data file
dataframe = pd.read_csv(base+tail, sep=",")

# Check data
print ("Interpretation data file: ", dataframe.dtypes)
if not set(to_plot).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")
if not set(["n_OFM3_max","n_OFM2_max","n_OFM1_max","n_source_max"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# Create empty plot
sns.set_theme()
cm = 2.54  # centimeters in inches
fig, axs = plt.subplots(4,5,figsize=(10, 8),dpi=300, sharex='col')
fig.subplots_adjust(top = 0.95, bottom = 0.06, left = 0.08, right = 0.90, hspace=0.4, wspace=0.4)

# Plot requested columns
# Structure of input file -> 9*8 combinations -> pick subset
#name,initial_craton_distance,initial_fault_geometry,start_migration,migration_direction,start_border_fault,max_source_basins,max_source_host_basins,max_OFM3,max_OFM2,n_OFM12_max,end_migration,max_source
#initial_fault_geometry,start_left_border_fault,start_right_border_fault,end_left_border_fault,end_right_border_fault,start_migration,end_migration,migration_direction,start_oceanic_spreading,n_source_max,n_source_host_max,n_OFM3_max,n_OFM1_max,n_OFM2_max,n_OFM12_max

# First column
sns.scatterplot(data=dataframe,x="initial_craton_distance",y="n_source_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[0,0],legend=False)
sns.scatterplot(data=dataframe,x="initial_craton_distance",y="n_source_host_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[1,0],legend=False)
sns.scatterplot(data=dataframe,x="initial_craton_distance",y="n_OFM3_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[2,0],legend=False)
sns.scatterplot(data=dataframe,x="initial_craton_distance",y="n_OFM12_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[3,0],legend=False)

# Second column
sns.scatterplot(data=dataframe,x="start_migration",y="n_source_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[0,1],legend=False)
sns.scatterplot(data=dataframe,x="start_migration",y="n_source_host_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[1,1],legend=False)
sns.scatterplot(data=dataframe,x="start_migration",y="n_OFM3_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[2,1],legend=False)
sns.scatterplot(data=dataframe,x="start_migration",y="n_OFM12_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[3,1],legend=False)

# Third column
sns.scatterplot(data=dataframe,x="end_migration",y="n_source_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[0,2],legend=False)
sns.scatterplot(data=dataframe,x="end_migration",y="n_source_host_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[1,2],legend=False)
sns.scatterplot(data=dataframe,x="end_migration",y="n_OFM3_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[2,2],legend=False)
sns.scatterplot(data=dataframe,x="end_migration",y="n_OFM12_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[3,2],legend=False)

## Fourth column
sns.scatterplot(data=dataframe,x="migration_direction",y="n_source_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[0,3],legend=False)
##axs[0,3].xaxis.set_visible(False)
##axs[0,3].set_xlabel("")
sns.scatterplot(data=dataframe,x="migration_direction",y="n_source_host_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[1,3],legend=False)
#sns.move_legend(axs[1,3], "upper left", bbox_to_anchor=(1, 1)) #,title=None, frameon=False)
sns.scatterplot(data=dataframe,x="migration_direction",y="n_OFM3_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[2,3],legend=False)
sns.scatterplot(data=dataframe,x="migration_direction",y="n_OFM12_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[3,3],legend=False)

## Fifth column
sns.scatterplot(data=dataframe,x="start_right_border_fault",y="n_source_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[0,4],legend=False)
sns.scatterplot(data=dataframe,x="start_right_border_fault",y="n_source_host_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[1,4],legend=True)
sns.scatterplot(data=dataframe,x="start_right_border_fault",y="n_OFM3_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[2,4],legend=False)
sns.scatterplot(data=dataframe,x="start_right_border_fault",y="n_OFM12_max",size="n_OFM12_max",sizes=(0,200),hue="n_OFM12_max",ax=axs[3,4],legend=False)

# Ranges and labels of the axes
ftsize = 6
for ax in axs.reshape(-1):
  if ax.get_xlabel() == 'initial_craton_distance':
    ax.set_xlim(345,555.) # km
    ax.set_xticks([400,450,500])
    ax.set_xlabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'initial_fault_geometry':
    ax.set_xlabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_migration':
#    ax.set_xlim(4.90,10.10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'migration_direction':
#    ax.set_xticks(["L","C","R"])
    ax.set_xlabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_left_border_fault':
    ax.set_xlim(-0.10,10.10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_right_border_fault':
    ax.set_xlim(-0.10,10.10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_source_max':
    ax.set_xlim(-0.1,10.1) # -
    ax.set_xlabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_source_host_max':
    ax.set_xlim(-0.1,10.1) # -
    ax.set_xlabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM3_max':
    ax.set_xlim(-1.05,5.05) # -
    ax.set_xlabel("Max. nr of OFM3 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM2_max':
    ax.set_xlim(-0.05,5.05) # -
    ax.set_xlabel("Max. nr of OFM2 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OMF1_max':
    ax.set_xlim(-0.05,5.05) # -
    ax.set_xlabel("Max. nr of OFM1 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM12_max':
    ax.set_xlim(-0.05,7.05) # -
    ax.set_xlabel("Max. nr of OFM12 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'end_migration':
    ax.set_xlim(9.75,25.25) # My
    ax.set_xticks([10,15,20,25])
    ax.set_xlabel("End rift migration [My]",weight="bold",fontsize=ftsize)
  
  if ax.get_ylabel() == 'initial_craton_distance':
    ax.set_ylim(345,555) # km
    ax.set_yticks([400,450,500])
    ax.set_ylabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
  if ax.get_ylabel() == 'initial_fault_geometry':
    ax.set_ylabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_migration':
    ax.set_ylim(-0.10,10.10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'migration_direction':
#    ax.set_yticks(["L","C","R"])
    ax.set_ylabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_left_border_fault':
    ax.set_ylim(-0.10,10.10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_right_border_fault':
    ax.set_ylim(-0.10,10.10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_border_fault':
    ax.set_ylim(-0.25,25.25) # My
    ax.set_yticks([0,10,20,25])
    ax.set_ylabel("Start border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_source_max':
    ax.set_ylim(-0.1,10.1) # -
    ax.set_ylabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_source_host_max':
    ax.set_ylim(-0.1,10.1) # -
    ax.set_ylabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_OFM3_max':
    ax.set_ylim(-1.05,5.05) # -
    ax.set_ylabel("Max. nr of OFM3 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_OFM2_max':
    ax.set_ylim(-0.05,5.05) # -
    ax.set_ylabel("Max. nr of OFM2 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_OMF1_max':
    ax.set_ylim(-0.05,5.05) # -
    ax.set_ylabel("Max. nr of OFM1 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_OFM12_max':
    ax.set_ylim(-0.07,7.07) # -
    ax.set_ylabel("Max. nr of OFM12 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'end_migration':
    ax.set_ylim(9.75,25.25) # My
    ax.set_yticks([10,15,20,25])
    ax.set_ylabel("End rift migration [My]",weight="bold",fontsize=ftsize)

# Axis labels
#ax = plt.gca()
#ax.get_yaxis().get_major_formatter().set_useOffset(False)
#plt.ticklabel_format(axis='y',useOffset=False)
#plt.xticks(np.arange(0,30,5))
##plt.yticks([0,50,100,150,200,210])
#plt.show()

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
plt.savefig(output_name + '_CERI_cratons.png')    
print ("Output in: ", output_name + '_CERI_cratons.png')
