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

output_name = '5po_fixed_plusinf_cuttonewOS_'

# File name
# real file
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_cuttonewOS.csv"

###### Model names ######
# List left-migrating before right-migrating sims
models = [
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
]


# Use the seaborn theme,
sns.set_theme()
# but tweak the colors a bit
color_1 = (0.2980392156862745, 0.4470588235294118, 0.6901960784313725) #76,114,176. 
color_3 = (0.3333333333333333, 0.6588235294117647, 0.40784313725490196) #85,168,104
# A 20% darker version of the above colors for the lines of the regression
#60%:rgb(30, 45, 70)(0.117647058823529, 0.176470588235294, 0.274509803921569) 40%:rgb(46, 68, 106)(0.180392156862745, 0.266666666666667, 0.415686274509804) 30%:rgb(53, 79, 123)
color_2 = (0.207843137254902, 0.309803921568627, 0.482352941176471) 
#60%:rgb(34, 67, 42) 20%:rgb(68, 134, 83)(0.266666666666667, 0.525490196078431, 0.325490196078431) 40%:rgb(51, 101, 62)(0.2, 0.396078431372549, 0.243137254901961) 30%:rgb(59, 118, 73)
color_4 = (0.231372549019608, 0.462745098039216, 0.286274509803922) 

# Create empty plot
n_columns = 2
n_rows = 4
fig, axs = plt.subplots(n_rows,n_columns,figsize=(2*n_columns, 2*n_rows),dpi=300, sharex='col', sharey='row')
fig.subplots_adjust(hspace = 0.05)
fig.subplots_adjust(wspace = 0.05)

###### Loop over requested models ######
total_OFMs = np.zeros((2,4))
total_OFM1s = np.zeros((2,4))
total_OFM2s = np.zeros((2,4))
total_timesteps_OFMs = np.zeros((2,4))
for m in models:

  print ("Reading model: ", m)
  path = base + m

  if Path(path).exists():  
    stat_files = sorted(Path(path).glob('*stats_2*'))
    #print("Stats files", stat_files)
    summary_files = sorted(Path(path).glob('*stats_summary_cuttonewOS_2*'))
    #print("Summary files", summary_files)

  if len(summary_files) == 1:
    filename = path + "/" + summary_files[0].name
    dataframe_summary = pd.read_csv(filename)

    start_spreading_step = np.int64(dataframe_summary["start_oceanic_spreading"][0] * 2)
    print ("Start oceanic spreading: ", start_spreading_step)

  else:
    print ("Multiple or no summary files for model: ", m)
    exit()

  if len(stat_files) == 1:
    
    # NA sims (5p) are plotted on the left, W (5o) on the right
    column_number = 0
    if "5o" in m:
      column_number = 1
    # The index for the distance (0 = 50 km = edge at 400 km) 
    distance_number = 0
    if "craton450" in m:
      distance_number = 1
    elif "craton500" in m:
      distance_number = 2
    elif "craton2000" in m:
      distance_number = 3

    # Read the data file
    filename = path + "/" + stat_files[0].name
    dataframe_stats = pd.read_csv(filename, sep=",") #,converters={'time': int,'n_OFM1': int,'n_OFM2': int, 'n_OFM3': int})
    if dataframe_stats.isnull().values.any():
      print ("Statistics file contains NaN")
      exit()

    # Limit the data by the start of oceanic spreading
    # and quantify favorability
    if start_spreading_step <= 50:
      dataframe_stats_cut = dataframe_stats[dataframe_stats["time"].le((start_spreading_step))]
      tmp_total_OFMs = dataframe_stats_cut['n_OFM1'].sum() + dataframe_stats_cut['n_OFM2'].sum() + dataframe_stats_cut['n_OFM3'].sum()
      tmp_total_OFM1s = dataframe_stats_cut['n_OFM1'].sum()
      tmp_total_OFM2s = dataframe_stats_cut['n_OFM2'].sum()
      tmp_timesteps_OFMs = np.count_nonzero(dataframe_stats_cut['n_OFM1'] + dataframe_stats_cut['n_OFM2'] + dataframe_stats_cut['n_OFM3'])
    else:
      tmp_total_OFMs = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
      tmp_total_OFM1s = dataframe_stats['n_OFM1'].sum()
      tmp_total_OFM2s = dataframe_stats['n_OFM2'].sum()
      dataframe_stats['n_OFM123'] = dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'] + dataframe_stats['n_OFM3']
      tmp_timesteps_OFMs = np.count_nonzero(dataframe_stats['n_OFM123'])

    # print("Total all OFMs:", dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum())
    # print("Total all OFM1s:", dataframe_stats['n_OFM1'].sum())
    # print("Total all OFM2s:", dataframe_stats['n_OFM2'].sum())
    # print("Total all timesteps with OFMs:", np.count_nonzero(dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'] + dataframe_stats['n_OFM3']))
    # print("Total OFMs cuttonewOS:", tmp_total_OFMs)
    # print("Total OFM1s cuttonewOS:", tmp_total_OFM1s)
    # print("Total OFM2s cuttonewOS:", tmp_total_OFM2s)
    # print("Total timesteps with OFMs cuttonewOS:", tmp_timesteps_OFMs)

    # Store data using the indices derived above
    total_OFMs[column_number][distance_number] += tmp_total_OFMs
    total_OFM1s[column_number][distance_number] += tmp_total_OFM1s
    total_OFM2s[column_number][distance_number] += tmp_total_OFM2s
    total_timesteps_OFMs[column_number][distance_number] += tmp_timesteps_OFMs

  else:
    print ("Multiple or no stats files for model: ", m)
    exit()


# Average the total OFMs and OFM1s per suite
total_OFMs = total_OFMs/9.
total_OFM1s = total_OFM1s/9.
total_OFM2s = total_OFM2s/9.
total_timesteps_OFMs = total_timesteps_OFMs/9.

##### PLOT #####
## Plot the average total OFMs and OFM1s per suite
distances = np.zeros(4)
distances[0] = 50
distances[1] = 100
distances[2] = 150
distances[3] = 200

axs[0][0].scatter(distances,total_OFMs[0], color=color_1, label="Total OFMs")
axs[0][1].scatter(distances,total_OFMs[1], color=color_1)

axs[1][0].scatter(distances,total_OFM1s[0], color=color_3, label="Total OFM1s")
axs[1][1].scatter(distances,total_OFM1s[1], color=color_3)

axs[2][0].scatter(distances,total_OFM2s[0], color=color_4, label="Total OFM2s")
axs[2][1].scatter(distances,total_OFM2s[1], color=color_4)

axs[3][0].scatter(distances,total_timesteps_OFMs[0], color=color_2, label="Timesteps OFMs")
axs[3][1].scatter(distances,total_timesteps_OFMs[1], color=color_2)

# Ranges and labels of the axes
craton_distance_labels = ["50", "100", "150", r"$\infty$"]
ftsize = 10
axs[0][0].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize)
axs[0][1].set_title("Wide",weight="bold",fontsize=ftsize)

axs[0][0].set_ylabel("Av. total OFMs",weight="bold",fontsize=ftsize)
axs[0][0].set_yticks([0,10,20,30,40])
axs[1][0].set_ylabel("Av. total OFM1s",weight="bold",fontsize=ftsize)
axs[1][0].set_yticks([0,2,4,6])
axs[2][0].set_ylabel("Av. total OFM2s",weight="bold",fontsize=ftsize)
axs[2][0].set_yticks([0,4,8,12,16])
axs[3][0].set_xlabel("Craton edge distance",weight="bold",fontsize=ftsize)
axs[3][0].set_xticks([50,100,150,200])
axs[3][0].set_xticklabels(["50","100","150","inf"])

axs[3][1].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize)
axs[3][1].set_xticks([50,100,150,200])
axs[3][1].set_xticklabels(["50","100","150","inf"])

axs[3][0].set_ylabel("Av. timesteps with OFMs",weight="bold",fontsize=ftsize)
axs[3][0].set_yticks([0,5,10,15,20,25])

##### SAVE #####
## Save figure
plt.savefig(output_name + '_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + '_CERI_cratons.png')

## Print and save the data
print ("Average total OFMs: ", total_OFMs)
print ("Average total OFM1s: ", total_OFM1s)
print ("Average total timesteps with OFMs: ", total_timesteps_OFMs)
# Data order:
# NA-50km
# NA-100km
# NA-150km
# NA-inf
# W-50km
# W-100km
# W-150km
# W-inf
total_OFMs.tofile(output_name + '_average_total_OFMs_CERI_cratons.csv', sep=' ')
print ("Data in: ", output_name + '_average_total_OFMs_CERI_cratons.csv')
total_OFM1s.tofile(output_name + '_average_total_OFM1s_CERI_cratons.csv', sep=' ')
print ("Data in: ", output_name + '_average_total_OFM1s_CERI_cratons.csv')
total_timesteps_OFMs.tofile(output_name + '_average_total_timesteps_OFMs_CERI_cratons.csv', sep=' ')
print ("Data in: ", output_name + '_average_total_timesteps_OFMs_CERI_cratons.csv')