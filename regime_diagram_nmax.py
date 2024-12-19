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
print ("Seaborn version: ", sns.__version__)

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

output_name = '5p_fixed_regime_diagram_nmax_duration'

# File name
# test file
tail = r"5p_fixed_CERI_craton_analysis.txt"
# real file
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"

# Structure of input file: 3x9 rows of the following columns:
# initial_craton_distance,initial_fault_geometry,start_left_border_fault,start_right_border_fault,end_left_border_fault,end_right_border_fault,start_migration,end_migration,migration_direction,start_oceanic_spreading,n_source_max,n_source_host_max,n_OFM3_max,n_OFM1_max,n_OFM2_max,n_OFM12_max
columns_to_plot = ['initial_craton_distance', 'migration_duration', 'migration_direction', 'left_border_fault_duration', 'right_border_fault_duration']

# Read the data file
dataframe = pd.read_csv(base+tail, sep=",")

# Compute durations
dataframe['migration_duration'] = dataframe['end_migration'] - dataframe['start_migration']
dataframe['left_border_fault_duration'] = dataframe['end_left_border_fault'] - dataframe['start_left_border_fault']
dataframe['right_border_fault_duration'] = dataframe['end_right_border_fault'] - dataframe['start_right_border_fault']

# Check data
#print ("Interpretation data file: ", dataframe.dtypes)
if not set(columns_to_plot).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")
if not set(["n_OFM3_max","n_OFM2_max","n_OFM1_max","n_source_max","source_max"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# Create empty plot
sns.set_theme()
cm = 2.54  # centimeters in inches
n_columns = len(columns_to_plot)
fig, axs = plt.subplots(4,n_columns,figsize=(2*n_columns, 8),dpi=300, sharex='col', sharey='row')
#fig.subplots_adjust(top = 0.95, bottom = 0.06, left = 0.08, right = 0.90, hspace=0.4, wspace=0.4)

# Plot requested columns by looping over column names
for i in range(n_columns):
  sns.scatterplot(data=dataframe,x=columns_to_plot[i],y="n_source_max",size="source_max",sizes=(20,200),hue="n_OFM12_max",ax=axs[0,i],legend=False, alpha=0.7)
  if i == n_columns-1:
    sns.scatterplot(data=dataframe,x=columns_to_plot[i],y="n_source_host_max",size="source_max",sizes=(20,200),hue="n_OFM12_max",ax=axs[1,i],legend="brief", alpha=0.7)
    #sns.move_legend(axs[1,i], "upper right") #, bbox_to_anchor=(1, 1), fontsize=8) #,title=None, frameon=False)
  else:
    sns.scatterplot(data=dataframe,x=columns_to_plot[i],y="n_source_host_max",size="source_max",sizes=(20,200),hue="n_OFM12_max",ax=axs[1,i],legend=False, alpha=0.7)
  sns.scatterplot(data=dataframe,x=columns_to_plot[i],y="n_OFM3_max",size="source_max",sizes=(20,200),hue="n_OFM12_max",ax=axs[2,i],legend=False, alpha=0.7)
  sns.scatterplot(data=dataframe,x=columns_to_plot[i],y="n_OFM12_max",size="source_max",sizes=(20,200),hue="n_OFM12_max",ax=axs[3,i],legend=False, alpha=0.7)


# Ranges and labels of the axes
# TODO Would be great not to repeat this for both the x and y axis.
ftsize = 6
for ax in axs.reshape(-1):
  if ax.get_xlabel() == 'initial_craton_distance':
    ax.set_xlim(345,555.) # km
    ax.set_xticks([400,450,500])
    ax.set_xlabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'initial_fault_geometry':
    ax.set_xlabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_migration':
    ax.set_xlim(4.90,10.10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'migration_direction':
    ax.margins(x=0.2)
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
  elif ax.get_xlabel() == 'migration_duration':
    ax.set_xlim(0,25) # My
    ax.set_xticks([0,12.5,25])
    ax.set_xlabel("Rift migration duration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'left_border_fault_duration':
    ax.set_xlim(0,25) # My
    ax.set_xticks([0,12.5,25])
    ax.set_xlabel("Left border fault duration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'right_border_fault_duration':
    ax.set_xlim(0,25) # My
    ax.set_xticks([0,12.5,25])
    ax.set_xlabel("Right border fault duration [My]",weight="bold",fontsize=ftsize)
  
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
    ax.margins(x=0.2)
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
  elif ax.get_ylabel() == 'migration_duration':
    ax.set_ylim(0,25) # My
    ax.set_yticks([0,12.5,25])
    ax.set_ylabel("Rift migration duration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'left_border_fault_duration':
    ax.set_ylim(0,25) # My
    ax.set_yticks([0,12.5,25])
    ax.set_ylabel("Left border fault duration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'right_border_fault_duration':
    ax.set_ylim(0,25) # My
    ax.set_yticks([0,12.5,25])
    ax.set_ylabel("Right border fault duration [My]",weight="bold",fontsize=ftsize)

## Name the png according to the plotted field
plt.savefig(output_name + '_CERI_cratons.png')    
print ("Output in: ", output_name + '_CERI_cratons.png')
