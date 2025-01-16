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

output_name = '5o_fixed_regime_diagram_nmax_duration'

# File name
# test file
tail = r"5p_fixed_CERI_craton_analysis.txt"
# real file
tail = r"5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"

# Structure of input file: 4x9 rows of the following columns:
# initial_craton_distance,initial_fault_geometry,start_left_border_fault,start_right_border_fault,end_left_border_fault,end_right_border_fault,start_migration,end_migration,migration_direction,start_oceanic_spreading,n_source_max,n_source_host_max,n_OFM3_max,n_OFM1_max,n_OFM2_max,n_OFM12_max
columns_to_plot = ['initial_craton_distance', 'migration_duration', 'migration_direction', 'left_border_fault_duration', 'right_border_fault_duration']
rows_to_plot = ['n_source_max', 'n_source_host_max', 'n_OFM3_max', 'n_OFM12_max']

# Whether or not to set limits for and format the axes.
# Setting it to False helps in spotting unexpected outliers.
set_axes = True

# Read the data file
dataframe = pd.read_csv(base+tail, sep=",", comment='#')

# Some border faults live on till the end of the simulation, they were given a value of 50 My.
# Same for rifts, some do not stabilize within the model time.
# To compute the duration, set their end time to 25 My, the end of the model run.
dataframe.loc[dataframe["end_migration"] > 25, "end_migration"] = 25
dataframe.loc[dataframe["end_left_border_fault"] > 25, "end_left_border_fault"] = 25
dataframe.loc[dataframe["end_right_border_fault"] > 25, "end_right_border_fault"] = 25

# Compute durations
dataframe['migration_duration'] = dataframe['end_migration'] - dataframe['start_migration']
dataframe['left_border_fault_duration'] = dataframe['end_left_border_fault'] - dataframe['start_left_border_fault']
dataframe['right_border_fault_duration'] = dataframe['end_right_border_fault'] - dataframe['start_right_border_fault']

# Check data
if not set(columns_to_plot).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")
if not set(["n_OFM3_max","n_OFM2_max","n_OFM1_max","n_source_max","source_max"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# The runs without a craton have an artificial craton distance of 2000 km. Replace this value
# with 550 km, but label axis as "infinite".
dataframe.loc[dataframe['initial_craton_distance'] == 2000, 'initial_craton_distance'] = 550

# Order data according to migration direction so that direction axes have the same order
# Order in which style and hue are applied according to migration direction
order = ["L", "C", "R"]
dataframe.migration_direction = dataframe.migration_direction.astype("category")
dataframe.migration_direction = dataframe.migration_direction.cat.set_categories(order)
dataframe.sort_values(["initial_fault_geometry"])

# For the regression plots, we only want to use the craton distances of 400, 450 and 500 km,
# as these are the ones that were actually in the model domain. Select this subset:
dataframe_cratons = dataframe[dataframe["initial_craton_distance"].isin([400,450,500])]
# Some border faults live on till the end of the simulation, they were given a value of 50 My.
# This also skews the regression, so remove them.
# TODO this isn't necessary anymore, as we already restrict the end time to 25 My
dataframe_left_border_fault = dataframe_cratons[dataframe_cratons["left_border_fault_duration"] <= 25]
dataframe_right_border_fault = dataframe_cratons[dataframe_cratons["right_border_fault_duration"] <= 25]
# Same for rifts, some do not stabilize within the model time.
dataframe_migration = dataframe_cratons[dataframe_cratons["migration_duration"] <= 25]

# Use the seaborn theme,
sns.set_theme()
# but tweak the colors a bit
# The colors of the data split according to migration direction
color_left = (0.2980392156862745, 0.4470588235294118, 0.6901960784313725) #76,114,176. 
color_right = (0.3333333333333333, 0.6588235294117647, 0.40784313725490196) #85,168,104
# A 20% darker version of the above colors for the lines of the regression
#60%:rgb(30, 45, 70)(0.117647058823529, 0.176470588235294, 0.274509803921569) 40%:rgb(46, 68, 106)(0.180392156862745, 0.266666666666667, 0.415686274509804) 30%:rgb(53, 79, 123)
color_left_darker = (0.207843137254902, 0.309803921568627, 0.482352941176471) 
#60%:rgb(34, 67, 42) 20%:rgb(68, 134, 83)(0.266666666666667, 0.525490196078431, 0.325490196078431) 40%:rgb(51, 101, 62)(0.2, 0.396078431372549, 0.243137254901961) 30%:rgb(59, 118, 73)
color_right_darker = (0.231372549019608, 0.462745098039216, 0.286274509803922) 

# Create empty plot
n_columns = len(columns_to_plot)
n_rows = len(rows_to_plot)
fig, axs = plt.subplots(4,n_columns,figsize=(2*n_columns, 2*n_rows),dpi=300, sharex='col', sharey='row')

# Regression confidence interval (0 = don't plot)
confidence_interval = 0
# Which markers for which migration direction
markers = {'L': 'o', 'C':'X', 'R': 's'}

# Repeated parameters for regression
reg_prms = {"scatter":False,"robust":False,"order":1,"ci":confidence_interval}

# Plot requested columns by looping over column names
for i in range(n_columns):
  for j in range(n_rows):
    # Plot the data for all models
    sns.scatterplot(data=dataframe,x=columns_to_plot[i],y=rows_to_plot[j],size="source_max",sizes=(20,200),hue="migration_direction",hue_order=order,style="migration_direction",style_order=order,markers=markers,ax=axs[j,i],legend=False, alpha=0.7)
      
    # Do a regression on the models with cratons, with a separated regression for each migration direction
    # Does not work categorical data.
    if columns_to_plot[i] != "migration_direction" and rows_to_plot[j] != "migration_direction" and columns_to_plot[i] != "initial_fault_geometry" and rows_to_plot[j] != "initial_fault_geometry":
      if columns_to_plot[i] == "left_border_fault_duration" or rows_to_plot[j] == "left_border_fault_duration":
        # Note that with lmplot, the different fits for migration direction can be calculated in one go.
        sns.regplot(data=dataframe_left_border_fault[dataframe_left_border_fault["migration_direction"].isin(["L"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_left_darker),ax=axs[j,i],**reg_prms)
        sns.regplot(data=dataframe_left_border_fault[dataframe_left_border_fault["migration_direction"].isin(["R"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_right_darker),ax=axs[j,i],**reg_prms)
      elif columns_to_plot[i] == "right_border_fault_duration" or rows_to_plot[j] == "right_border_fault_duration":
        sns.regplot(data=dataframe_right_border_fault[dataframe_right_border_fault["migration_direction"].isin(["L"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_left_darker),ax=axs[j,i],**reg_prms)
        sns.regplot(data=dataframe_right_border_fault[dataframe_right_border_fault["migration_direction"].isin(["R"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_right_darker),ax=axs[j,i],**reg_prms)
      elif columns_to_plot[i] == "migration_duration" or rows_to_plot[j] == "migration_duration":
        sns.regplot(data=dataframe_migration[dataframe_migration["migration_direction"].isin(["L"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_left_darker),ax=axs[j,i],**reg_prms)
        sns.regplot(data=dataframe_migration[dataframe_migration["migration_direction"].isin(["R"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_right_darker),ax=axs[j,i],**reg_prms)
      else:
        sns.regplot(data=dataframe_cratons[dataframe_cratons["migration_direction"].isin(["L"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_left_darker),ax=axs[j,i],**reg_prms)
        sns.regplot(data=dataframe_cratons[dataframe_cratons["migration_direction"].isin(["R"])],x=columns_to_plot[i],y=rows_to_plot[j],line_kws=dict(color=color_right_darker),ax=axs[j,i],**reg_prms)

# Ranges and labels of the axes
# TODO Would be great not to repeat this for both the x and y axis.
ftsize = 6
craton_distance_labels = ["50", "100", "150", r"$\infty$"]
# 5o settings
migration_duration_min = 0
migration_duration_max = 14
migration_duration_ticks = [0,7.0,14]
LBF_duration_min = 7
LBF_duration_max = 21
LBF_duration_ticks = [7.0,14.0,21]
RBF_duration_min = 2
RBF_duration_max = 22
RBF_duration_ticks = [2,7.0,12.0,17,22]
S_min = 0
S_max = 8
S_ticks = [0,2,4,6,8]
SH_min = 0
SH_max = 6
SH_ticks = [0,2,4,6]
OFM12_max = 4
OFM3_min = 0
# 5p settings
# migration_duration_min = 5
# migration_duration_max = 20
# migration_duration_ticks = [5.0,10.0,15.0,20]
# LBF_duration_min = 0
# LBF_duration_max = 25
# LBF_duration_ticks = [0,5,10,15,20,25]
# RBF_duration_min = 2
# RBF_duration_max = 22
# RBF_duration_ticks = [2,7.0,12.0,17,22]
# S_min = 2
# S_max = 10
# S_ticks = [2,4,6,8,10]
# OFM12_max = 7
# OFM3_min = -1
if set_axes:
  for ax in axs.reshape(-1):
    if ax.get_xlabel() == 'initial_craton_distance':
      ax.set_xlim(350,600.) # km
      ax.set_xticks([400,450,500,550])
      ax.set_xticklabels(craton_distance_labels)
      ax.set_xlabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'initial_fault_geometry':
      ax.set_xlabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'start_migration':
      ax.set_xlim(5.0,10.0) # My
      ax.set_xticks([0,5,10])
      ax.set_xlabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'migration_direction':
      ax.margins(x=0.2)
      ax.set_xlabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'start_left_border_fault':
      ax.set_xlim(-0.0,10.0) # My
      ax.set_xticks([0,5,10])
      ax.set_xlabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'start_right_border_fault':
      ax.set_xlim(-0.0,10.) # My
      ax.set_xticks([0,5,10])
      ax.set_xlabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_source_max':
      ax.set_xlim(S_min,S_max) # -
      ax.set_xticks(S_ticks)
      ax.set_xlabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_source_host_max':
      ax.set_xlim(SH_min,SH_max) # -
      ax.set_xticks(SH_ticks)
      ax.set_xlabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_OFM3_max':
      ax.set_xlim(OFM3_min,4.0) # -
      ax.set_xlabel("Max. nr of OFM3 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_OFM2_max':
      ax.set_xlim(-0.0,5.0) # -
      ax.set_xlabel("Max. nr of OFM2 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_OMF1_max':
      ax.set_xlim(-0.0,5.0) # -
      ax.set_xlabel("Max. nr of OFM1 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'n_OFM12_max':
      ax.set_xlim(-0.0,OFM12_max) # -
      ax.set_xlabel("Max. nr of OFM12 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'end_migration':
      ax.set_xlim(10,25) # My
      ax.set_xticks([10,15,20,25])
      ax.set_xlabel("End rift migration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'migration_duration':
      ax.set_xlim(migration_duration_min,migration_duration_max) # My
      ax.set_xticks(migration_duration_ticks)
      ax.set_xlabel("Rift migration duration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'left_border_fault_duration':
      ax.set_xlim(LBF_duration_min,LBF_duration_max) # My
      ax.set_xticks(LBF_duration_ticks)
      ax.set_xlabel("Left border fault duration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_xlabel() == 'right_border_fault_duration':
      ax.set_xlim(RBF_duration_min,RBF_duration_max) # My
      ax.set_xticks(RBF_duration_ticks)
      ax.set_xlabel("Right border fault duration [My]",weight="bold",fontsize=ftsize)
  
    if ax.get_ylabel() == 'initial_craton_distance':
      ax.set_ylim(350,600.) # km
      ax.set_yticks([400,450,500,550])
      ax.set_yticklabels(craton_distance_labels)
      ax.set_ylabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'initial_fault_geometry':
      ax.set_ylabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'start_migration':
      ax.set_ylim(-0.0,10.0) # My
      ax.set_yticks([0,5,10])
      ax.set_ylabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'migration_direction':
      ax.margins(x=0.2)
      ax.set_ylabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'start_left_border_fault':
      ax.set_ylim(-0.0,10.0) # My
      ax.set_yticks([0,5,10])
      ax.set_ylabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'start_right_border_fault':
      ax.set_ylim(-0.0,10.0) # My
      ax.set_yticks([0,5,10])
      ax.set_ylabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'start_border_fault':
      ax.set_ylim(-0,25) # My
      ax.set_yticks([0,10,20,25])
      ax.set_ylabel("Start border fault(s) [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_source_max':
      ax.set_ylim(S_min,S_max) # -
      ax.set_yticks(S_ticks)
      ax.set_ylabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_source_host_max':
      ax.set_ylim(SH_min,SH_max) # -
      ax.set_yticks(SH_ticks)
      ax.set_ylabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_OFM3_max':
      ax.set_ylim(OFM3_min,4.0) # -
      ax.set_ylabel("Max. nr of OFM3 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_OFM2_max':
      ax.set_ylim(-0.0,5.0) # -
      ax.set_ylabel("Max. nr of OFM2 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_OMF1_max':
      ax.set_ylim(-0.0,5.0) # -
      ax.set_ylabel("Max. nr of OFM1 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'n_OFM12_max':
      ax.set_ylim(-0.0,OFM12_max) # -
      ax.set_ylabel("Max. nr of OFM12 [-]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'end_migration':
      ax.set_ylim(10,25) # My
      ax.set_yticks([10,15,20,25])
      ax.set_ylabel("End rift migration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'migration_duration':
      ax.set_ylim(migration_duration_min,migration_duration_max) # My
      ax.set_yticks(migration_duration_ticks)
      ax.set_ylabel("Rift migration duration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'left_border_fault_duration':
      ax.set_ylim(LBF_duration_min,LBF_duration_max) # My
      ax.set_yticks(LBF_duration_ticks)
      ax.set_ylabel("Left border fault duration [My]",weight="bold",fontsize=ftsize)
    elif ax.get_ylabel() == 'right_border_fault_duration':
      ax.set_ylim(RBF_duration_min,RBF_duration_max) # My
      ax.set_yticks(RBF_duration_ticks)
      ax.set_ylabel("Right border fault duration [My]",weight="bold",fontsize=ftsize)

## Name the png according to the plotted field
plt.savefig(output_name + '_CERI_cratons.png')    
print ("Output in: ", output_name + '_CERI_cratons.png')
