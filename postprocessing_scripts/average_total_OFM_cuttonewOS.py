# -*- coding: utf-8 -*-
"""
Created on Tue 9 Dec 2025 by Anne Glerum
Read the files
5{o,p}_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton{4,5}{5,0}0000.0_A0.25_seed*_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_stats_summary_cuttonewOS_*.csv
5{o,p}_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton{4,5}{5,0}0000.0_A0.25_seed*_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_stats_*.csv
for each simulation.
Report the average total nr of OFMs per model suite (rift type and craton edge distance).
"""
from itertools import count
from tokenize import Double
import numpy as np
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
# Scientific color maps
from cmcrameri import cm
from os.path import exists
from pathlib import Path
from sys import exit
import io
import re
import pandas as pd
import seaborn as sns
plt.rcParams["font.family"] = "Arial"

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

output_name = '5po_fixed_plusinf_average_total_OFMs_cuttonewOS_'

# File name
# real file
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_cuttonewOS.csv"

###### Model names ######
# List left-migrating before right-migrating sims
models = [




#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',








]

""" # Read the data file
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

# Add index column
#dataframe['index'] = dataframe[

# Check data
if not set(["n_OFM3_max","n_OFM2_max","n_OFM1_max","n_source_max","source_max"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# The runs without a craton have an artificial craton distance of 2000 km. Replace this value
# with 550 km, but label axis as "infinite".
dataframe.loc[dataframe['initial_craton_distance'] == 2000, 'initial_craton_distance'] = 550 """

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
n_columns = 2
n_rows = 1
fig, axs = plt.subplots(n_rows,n_columns,figsize=(2*n_columns, 2*n_rows),dpi=300, sharex='col', sharey='row')
fig.subplots_adjust(hspace = 0.05)
fig.subplots_adjust(wspace = 0.05)

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
counter = 0
palette_n_OFM = sns.color_palette(palette=colors)

###### Loop over requested models ######
total_OFMs = np.zeros((2,4))
for m in models:

  print ("Reading model: ", m)
  # NA sims (5p) are plotted on the left, W (5o) on the right
  column_number = 0
  if "5o" in m:
    column_number = 1
  #model_index = 0

  path = base + m
  if Path(path).exists():  
    stat_files = sorted(Path(path).glob('*stats_2*'))
    ASPECT_statistics_file = path + '/statistics'
  if len(stat_files) == 1:

    # Read the data file
    filename = path + "/" + stat_files[0].name
    dataframe_stats = pd.read_csv(filename, sep=",") #,converters={'time': int,'n_OFM1': int,'n_OFM2': int, 'n_OFM3': int})
    if "craton400" in m:
      dataframe_stats['initial_craton_distance'] = 50
      total_OFMs[column_number][0] = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
    elif "craton450" in m:
      dataframe_stats['initial_craton_distance'] = 100
      total_OFMs[column_number][1] = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
    elif "craton500" in m:
      dataframe_stats['initial_craton_distance'] = 150
      total_OFMs[column_number][2] = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
    else:
      dataframe_stats['initial_craton_distance'] = 2000
      total_OFMs[column_number][3] = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
    if "1236549" in m:
      model_index = column_number * 9 + 0
      sim_color = color1
    elif "2323432" in m:
      model_index = column_number * 9 + 1
      sim_color = color2
    elif "2349871" in m:
      model_index = column_number * 9 + 2
      sim_color = color3
    elif "2928465" in m:
      model_index = column_number * 9 + 3
      sim_color = color4
    elif "3458045" in m:
      model_index = column_number * 9 + 4
      sim_color = color5
    elif "5346276" in m:
      model_index = column_number * 9 + 5
      sim_color = color6
    elif "7646354" in m:
      model_index = column_number * 9 + 6
      sim_color = color7
    elif "9023857" in m:
      model_index = column_number * 9 + 7
      sim_color = color8
    elif "9872345" in m:
      model_index = column_number * 9 + 8
      sim_color = color9
    dataframe_stats['time'] = dataframe_stats['time'].div(2)
    dataframe_stats['n_OFM123'] = dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'] + dataframe_stats['n_OFM3']
    dataframe_stats = dataframe_stats.assign(**{"index": counter})

    counter += 1

  else:
    print ("Multiple or no summary files for model: ", m)

"""   # Plot border fault activity and migration over time
  dy = -0.1
  if (column_number == 0 and n_400 > 1) or (column_number == 1 and n_450 > 1) or (column_number == 2 and n_500 > 1) or (column_number == 3 and n_2000 > 1):
    dy = 0.1
  dataframe_model = dataframe.iloc[model_index]
  border_fault_data = {'time': [dataframe_model['start_left_border_fault'],dataframe_model['end_left_border_fault'],
                                dataframe_model['start_right_border_fault'],dataframe_model['end_right_border_fault'],
                                dataframe_model['start_migration'],dataframe_model['end_migration']],
                       'value': [3 + dy, 3 + dy, 2 + dy, 2 + dy, 1 + dy, 1 + dy],
                       'type': ['LBF', 'LBF', 'RBF', 'RBF', 'MIG', 'MIG']}
  df_model_border_faults = pd.DataFrame(border_fault_data)
  if dy > 0:
    sns.lineplot(data=df_model_border_faults,x='time',y='value',hue='type',ax=axs[0,column_number],palette=palette_n_OFM,legend=False)
  else:
    sns.lineplot(data=df_model_border_faults,x='time',y='value',hue='type',style=True,dashes=[(2,2)],ax=axs[0,column_number],palette=palette_n_OFM,legend=False)
   

  # Plot source area over time
  if Path(ASPECT_statistics_file).exists():
    # The correct columns are selected with usecols.
    # When no visu output file name is given, the respective line will have a lot of
    # placeholder spaces. We need to remove them before genfromtxt can deal with the
    # statistics file. 
    with open(ASPECT_statistics_file) as f:
      clean_lines = (re.sub('\s+',' ',line) for line in f)
      t,source_area = np.genfromtxt(clean_lines, comments='#', usecols=(1,62), delimiter=' ', unpack=True)
    # Interpolate onto less timesteps so the dashes/dots of the lines are not distorted.
    mean_t = np.arange(0, 25e6, 25000)
    interpolated_source_area = np.interp(mean_t, t, source_area)
    # time in My and area in km2
    dataframe_ASPECT = pd.DataFrame({'time': mean_t/1e6, 'source_area': interpolated_source_area/1e6})

    if dy > 0:
      sns.lineplot(data=dataframe_ASPECT,x='time',y='source_area', color=sim_color, ax=axs[1,column_number],palette=palette_n_OFM,legend=False) 
    else:
      sns.lineplot(data=dataframe_ASPECT,x='time',y='source_area', color=sim_color, style=True, dashes=[(2,2)], ax=axs[1,column_number],palette=palette_n_OFM,legend=False) 

# Ranges and labels of the axes
# TODO Would be great not to repeat this for both the x and y axis.

craton_distance_labels = ["50", "100", "150", r"$\infty$"]
ftsize = 10
axs[0,0].set_title("50 km",weight="bold",fontsize=ftsize)
axs[0,1].set_title("100 km",weight="bold",fontsize=ftsize)
axs[0,2].set_title("150 km",weight="bold",fontsize=ftsize)
axs[0,3].set_title("inf",weight="bold",fontsize=ftsize)
fig.suptitle('Craton edge distance',weight="bold", fontsize=ftsize)
for ax in axs.reshape(-1):
  ax.tick_params(axis='both', labelsize=10)
  if ax.get_xlabel() == 'time':
    ax.set_xlim(0,27) # My
    ax.set_xticks([0,5,10,15,20,25])
    ax.set_xlabel("Time [My]",weight="bold",fontsize=1.5*ftsize)
  else:
    print ("This x-axis label wasn't expected.")
  
  if ax.get_ylabel() == 'type_OFM':
    ax.set_ylabel("OFM type [-]",weight="bold",fontsize=1.9*ftsize)
  elif ax.get_ylabel() == 'numtype_OFM':
    ax.set_ylabel("OFM type [-]",weight="bold",fontsize=1.9*ftsize)
    ax.set_ylim(0.5,3.5)
    ax.set_yticks([1,2,3])
    ax.set_yticklabels(["OFM1", "OFM2", "OFM3"])
  elif ax.get_ylabel() == 'source_area':
    ax.set_ylim(-2,72) # km2
    ax.set_yticks([0,10,20,30,40,50,60,70])
    ax.set_ylabel(r"Source area [km$^2$]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'value':
    ax.set_ylabel("Tectonic event [-]",weight="bold",fontsize=ftsize)
    ax.set_yticks([1,2,3])
    ax.set_yticklabels(["MIG","RBF","LBF"])
    ax.set_ylim(0.7,3.3)
  else:
    print ("This y-axis label wasn't expected.") """

# Average the total OFMs per suite
print ("Total OFMs: ", total_OFMs[0])
total_OFMs = total_OFMs/9.

## Plot the average total OFMs per suite
distances = np.zeros(4)
distances[0] = 50
distances[1] = 100
distances[2] = 150
distances[3] = 200
print ("Distances: ", distances)
print ("Average total OFMs: ", total_OFMs[0])
axs[0].scatter(distances,total_OFMs[0])
axs[1].scatter(distances,total_OFMs[1])

## Save figure
# Make sure the y-axes labels align left
#fig.align_ylabels(axs[:, 0])
plt.savefig(output_name + '_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + '_CERI_cratons.png')

## Save the data
# Data order:
# NA-50km
# NA-100km
# NA-150km
# NA-inf
# W-50km
# W-100km
# W-150km
# W-inf
total_OFMs.tofile(output_name + '_CERI_cratons.csv', sep=' ')
print ("Data in: ", output_name + '_CERI_cratons.csv')