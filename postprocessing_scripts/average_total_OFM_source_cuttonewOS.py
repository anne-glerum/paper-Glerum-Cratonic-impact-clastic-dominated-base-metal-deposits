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

output_name = '5po_fixed_noinf_cuttonewOS_'
output_name = '5po_fixed_plusinf_cuttonewOS_'

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



###### Loop over requested models ######
# TODO replace with better data structure
total_OFMs = np.zeros((2,4))
total_OFMs_L = np.zeros((2,4))
total_OFMs_R = np.zeros((2,4))
total_OFM1s = np.zeros((2,4))
total_OFM2s = np.zeros((2,4))
total_OFM12s_R = np.zeros((2,4))
total_OFM12s_L = np.zeros((2,4))
total_timesteps_OFM12s = np.zeros((2,4))
total_timesteps_OFM12s_L = np.zeros((2,4))
total_timesteps_OFM12s_R = np.zeros((2,4))
total_timesteps_OFMs = np.zeros((2,4))
n_R = np.zeros((2,4))
n_L = np.zeros((2,4))
max_source_area_R = np.zeros((2,4))
max_source_area_L = np.zeros((2,4))
max_source_area = np.zeros((2,4))
average_source_area = np.zeros((2,4))
total_border_fault_duration = np.zeros((2,4))
total_migration_duration = np.zeros((2,4))
total_migration_start = np.zeros((2,4))
total_max_nr_source_R = np.zeros((2,4))
total_max_nr_source_L = np.zeros((2,4))
total_max_nr_source = np.zeros((2,4))
total_nr_source = np.zeros((2,4))

for m in models:

  #print ("Reading model: ", m)
  path = base + m

  if Path(path).exists():  
    stat_files = sorted(Path(path).glob('*stats_2*'))
    #print("Stats files", stat_files)
    summary_files = sorted(Path(path).glob('*stats_summary_cuttonewOS_2*'))
    #print("Summary files", summary_files)

  if len(summary_files) == 1:
    filename = path + "/" + summary_files[0].name
    dataframe_summary = pd.read_csv(filename,comment="#")

    start_spreading_step = np.int64(dataframe_summary["start_oceanic_spreading"][0] * 2)
    #print ("Start oceanic spreading: ", start_spreading_step)
    migration_direction = dataframe_summary["migration_direction"][0]
    #print ("Migration direction: ", migration_direction)

    if migration_direction == "L":
      tmp_end_migration = 25. if dataframe_summary["end_left_border_fault"][0] > 25. else dataframe_summary["end_left_border_fault"][0]
      tmp_start_migration = dataframe_summary["start_left_border_fault"][0]
      border_fault_duration = tmp_end_migration - tmp_start_migration
    elif migration_direction == "R":
      tmp_end_border_fault = 25. if dataframe_summary["end_right_border_fault"][0] > 25. else dataframe_summary["end_right_border_fault"][0]
      tmp_start_migration = dataframe_summary["start_right_border_fault"][0]
      border_fault_duration = tmp_end_border_fault - tmp_start_migration

    
    tmp_end_migration = 25. if dataframe_summary["end_migration"][0] > 25. else dataframe_summary["end_migration"][0]
    migration_duration = tmp_end_migration - dataframe_summary["start_migration"][0]

    if migration_direction == "C":
      migration_duration = 0
      border_fault_duration = 0

    if border_fault_duration > 25 or border_fault_duration < 0:
      print ("Border fault duration longer than 25 My or shorter than 0 My for model: ", m)
    if migration_duration > 25 or migration_duration < 0:
      print ("Migration duration longer than 25 My or shorter than 0 My for model: ", m)

    print ("Border fault duration: ", border_fault_duration)
    print ("Migration duration: ", migration_duration)

  else:
    print ("Multiple or no summary files for model: ", m, len(summary_files))
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
      tmp_timesteps_OFM12s = np.count_nonzero(dataframe_stats_cut['n_OFM1'] + dataframe_stats_cut['n_OFM2'])
      tmp_timesteps_OFMs = np.count_nonzero(dataframe_stats_cut['n_OFM1'] + dataframe_stats_cut['n_OFM2'] + dataframe_stats_cut['n_OFM3'])
      tmp_n_source = dataframe_stats_cut['n_source'].max()
      tmp_sum_n_source = dataframe_stats_cut['n_source'].sum()
    else:
      tmp_total_OFMs = dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum()
      tmp_total_OFM1s = dataframe_stats['n_OFM1'].sum()
      tmp_total_OFM2s = dataframe_stats['n_OFM2'].sum()
      dataframe_stats['n_OFM123'] = dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'] + dataframe_stats['n_OFM3']
      tmp_timesteps_OFM12s = np.count_nonzero(dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'])
      tmp_timesteps_OFMs = np.count_nonzero(dataframe_stats['n_OFM123'])
      tmp_n_source = dataframe_stats['n_source'].max()
      tmp_sum_n_source = dataframe_stats['n_source'].sum()

    # print("Total all OFMs:", dataframe_stats['n_OFM1'].sum() + dataframe_stats['n_OFM2'].sum() + dataframe_stats['n_OFM3'].sum())
    # print("Total all OFM1s:", dataframe_stats['n_OFM1'].sum())
    # print("Total all OFM2s:", dataframe_stats['n_OFM2'].sum())
    # print("Total all timesteps with OFMs:", np.count_nonzero(dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2'] + dataframe_stats['n_OFM3']))
    # print("Total OFMs cuttonewOS:", tmp_total_OFMs)
    # print("Total OFM1s cuttonewOS:", tmp_total_OFM1s)
    # print("Total OFM2s cuttonewOS:", tmp_total_OFM2s)
    # print("Total timesteps with OFMs cuttonewOS:", tmp_timesteps_OFMs)
    print("Max nr source cuttonewOS:", tmp_n_source)
    print("Sum nr source cuttonewOS:", tmp_sum_n_source)

    # Store data using the indices derived above
    total_OFMs[column_number][distance_number] += tmp_total_OFMs
    total_OFM1s[column_number][distance_number] += tmp_total_OFM1s
    total_OFM2s[column_number][distance_number] += tmp_total_OFM2s
    total_timesteps_OFM12s[column_number][distance_number] += tmp_timesteps_OFM12s
    total_timesteps_OFMs[column_number][distance_number] += tmp_timesteps_OFMs
    if migration_direction == "R":
      total_OFMs_R[column_number][distance_number] += tmp_total_OFMs
      total_OFM12s_R[column_number][distance_number] += tmp_total_OFM1s + tmp_total_OFM2s
      total_timesteps_OFM12s_R[column_number][distance_number] += tmp_timesteps_OFM12s
      total_max_nr_source_R[column_number][distance_number] += tmp_n_source
      n_R[column_number][distance_number] += 1
    elif migration_direction == "L":
      total_OFMs_L[column_number][distance_number] += tmp_total_OFMs
      total_OFM12s_L[column_number][distance_number] += tmp_total_OFM1s + tmp_total_OFM2s
      total_timesteps_OFM12s_L[column_number][distance_number] += tmp_timesteps_OFM12s
      total_max_nr_source_L[column_number][distance_number] += tmp_n_source
      n_L[column_number][distance_number] += 1
    total_border_fault_duration[column_number][distance_number] += border_fault_duration
    total_migration_duration[column_number][distance_number] += migration_duration
    total_migration_start[column_number][distance_number] += tmp_start_migration
    total_max_nr_source[column_number][distance_number] += tmp_n_source
    total_nr_source[column_number][distance_number] += tmp_sum_n_source

    # Read the ASPECT statistics file
    filename = path + "/statistics"
    # Read in the topography of each timestep. 
    # The correct columns are selected with usecols.
    # When no visu output file name is given, the respective line will have a lot of
    # placeholder spaces. We need to remove them before genfromtxt can deal with the
    # statistics file. 
    with open(path+"/statistics") as f:
      clean_lines = (re.sub('\s+',' ',line) for line in f)
      t,source_area = np.genfromtxt(clean_lines, comments='#', usecols=(1,62), delimiter=' ', unpack=True)
    if start_spreading_step <= 50:
      mask = t > 0.5 * start_spreading_step
      source_area = source_area[mask]
    # Add the max and average topo over the timespan of one simulation
    max_source_area[column_number][distance_number] += source_area.max()
    average_source_area[column_number][distance_number] += np.average(source_area)
    if migration_direction == "R":
      max_source_area_R[column_number][distance_number] += source_area.max()
    elif migration_direction == "L":
      max_source_area_L[column_number][distance_number] += source_area.max()

  else:
    print ("Multiple or no stats files for model: ", m)
    exit()

# Print
print ("Nr. of right migrating rifts: ", n_R)
print ("Nr. of left migrating rifts: ", n_L)
#print ("Nr. of OFM12s right migrating rifts: ", total_OFM12s_R)
#print ("Nr. of OFM12s left migrating rifts: ", total_OFM12s_L)

# Average per migration direction
n_OFMs_R = np.zeros((2,1))
n_OFMs_L = np.zeros((2,1))
n_OFMs_R[0] = total_OFMs_R[0].sum()/n_R[0].sum()
n_OFMs_R[1] = total_OFMs_R[1].sum()/n_R[1].sum()
n_OFMs_L[0] = total_OFMs_L[0].sum()/n_L[0].sum()
n_OFMs_L[1] = total_OFMs_L[1].sum()/n_L[1].sum()

n_OFM12s_R = np.zeros((2,1))
n_OFM12s_L = np.zeros((2,1))
n_OFM12s_R[0] = total_OFM12s_R[0].sum()/n_R[0].sum()
n_OFM12s_R[1] = total_OFM12s_R[1].sum()/n_R[1].sum()
n_OFM12s_L[0] = total_OFM12s_L[0].sum()/n_L[0].sum()
n_OFM12s_L[1] = total_OFM12s_L[1].sum()/n_L[1].sum()

n_timesteps_OFM12s_R = np.zeros((2,1))
n_timesteps_OFM12s_L = np.zeros((2,1))
n_timesteps_OFM12s_R[0] = total_timesteps_OFM12s_R[0].sum()/n_R[0].sum()
n_timesteps_OFM12s_R[1] = total_timesteps_OFM12s_R[1].sum()/n_R[1].sum()
n_timesteps_OFM12s_L[0] = total_timesteps_OFM12s_L[0].sum()/n_L[0].sum()
n_timesteps_OFM12s_L[1] = total_timesteps_OFM12s_L[1].sum()/n_L[1].sum()

# Also convert to km2
n_max_source_area_R = np.zeros((2,1))
n_max_source_area_L = np.zeros((2,1))
n_max_source_area_R[0] = max_source_area_R[0].sum()/n_R[0].sum()/1e6
n_max_source_area_R[1] = max_source_area_R[1].sum()/n_R[1].sum()/1e6
n_max_source_area_L[0] = max_source_area_L[0].sum()/n_L[0].sum()/1e6
n_max_source_area_L[1] = max_source_area_L[1].sum()/n_L[1].sum()/1e6

n_max_nr_source_R = np.zeros((2,1))
n_max_nr_source_L = np.zeros((2,1))
n_max_nr_source_R[0] = total_max_nr_source_R[0].sum()/n_R[0].sum()
n_max_nr_source_R[1] = total_max_nr_source_R[1].sum()/n_R[1].sum()
n_max_nr_source_L[0] = total_max_nr_source_L[0].sum()/n_L[0].sum()
n_max_nr_source_L[1] = total_max_nr_source_L[1].sum()/n_L[1].sum()

# Average the total OFMs and OFM1s per suite
# This can give warnings when dividing zero by zero for the numbers
# split into left and right migrating rifts.
# However, the result is a NaN, which is not plotted,
# so it's okay. Other numbers are not affected.
total_OFMs = total_OFMs/9.
total_OFMs_R = total_OFMs_R/n_R
total_OFMs_L = total_OFMs_L/n_L
total_OFM1s = total_OFM1s/9.
total_OFM2s = total_OFM2s/9.
total_OFM12s = total_OFM1s + total_OFM2s
total_OFM12s_R = total_OFM12s_R/n_R
total_OFM12s_L = total_OFM12s_L/n_L
total_timesteps_OFM12s = total_timesteps_OFM12s/9.
total_timesteps_OFM12s_R = total_timesteps_OFM12s_R/n_R
total_timesteps_OFM12s_L = total_timesteps_OFM12s_L/n_L
total_timesteps_OFMs = total_timesteps_OFMs/9.
# Also convert to km2
max_source_area_R = max_source_area_R/n_R/1e6
max_source_area_L = max_source_area_L/n_L/1e6
max_source_area = max_source_area/9/1e6
average_source_area = average_source_area/9/1e6
total_border_fault_duration = total_border_fault_duration/9.
total_migration_duration = total_migration_duration/9.
total_migration_start = total_migration_start/9.
# One W-50 run does not migrate, so do not include it in averaging
total_border_fault_duration[1][0] = total_border_fault_duration[1][0]*9/8
total_migration_duration[1][0] = total_migration_duration[1][0]*9/8
total_migration_start[1][0] = total_migration_start[1][0]*9/8
total_max_nr_source_R = total_max_nr_source_R/n_R
total_max_nr_source_L = total_max_nr_source_L/n_L
total_max_nr_source = total_max_nr_source/9.
total_nr_source = total_nr_source/9.

##### PLOT #####
## Create empty plot for source area
n_columns = 8
n_rows = 3
fig, axs = plt.subplots(n_rows,n_columns,figsize=(2*n_columns, 2*n_rows),dpi=300, sharex='col', sharey='row')
fig.subplots_adjust(hspace = 0.05)
fig.subplots_adjust(wspace = 0.05)

## 
distances = np.zeros((2,4))
distances[0][0] = 50
distances[0][1] = 100
distances[0][2] = 150
distances[0][3] = 200
distances[1][0] = 50
distances[1][1] = 100
distances[1][2] = 150
distances[1][3] = 200

## Plot the average max and average source area per suite total OFMs and OFM1s per suite
axs[0][0].scatter(distances[0],max_source_area[0], c=distances[0], cmap="Blues")
axs[0][1].scatter(distances[1],max_source_area[1], c=distances[1], cmap="Blues")

axs[1][0].scatter(distances[0],average_source_area[0], c=distances[0], cmap="Greens")
axs[1][1].scatter(distances[1],average_source_area[1], c=distances[1], cmap="Greens")

axs[2][0].scatter(distances[0],max_source_area_R[0], c=distances[0], cmap="Grays", label="R", s=40, marker="s")
axs[2][1].scatter(distances[1],max_source_area_R[1], c=distances[1], cmap="Grays", label="R",s=40, marker="s")
axs[2][0].scatter(distances[0],max_source_area_L[0], c=distances[0], cmap="Grays", label="L", s=60, marker="o")
axs[2][1].scatter(distances[1],max_source_area_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

axs[0][2].scatter(total_border_fault_duration[0],max_source_area[0], c=distances[0], cmap="Blues")
axs[0][3].scatter(total_border_fault_duration[1],max_source_area[1], c=distances[1], cmap="Blues")

axs[1][2].scatter(total_border_fault_duration[0],average_source_area[0], c=distances[0], cmap="Greens")
axs[1][3].scatter(total_border_fault_duration[1],average_source_area[1], c=distances[1], cmap="Greens")

axs[2][2].scatter(total_border_fault_duration[0],max_source_area_R[0], c=distances[0], cmap="Grays", label="R", s=40, marker="s")
axs[2][3].scatter(total_border_fault_duration[1],max_source_area_R[1], c=distances[1], cmap="Grays", label="R", s=40, marker="s")
axs[2][2].scatter(total_border_fault_duration[0],max_source_area_L[0], c=distances[0], cmap="Grays", label="L", s=60, marker="o")
axs[2][3].scatter(total_border_fault_duration[1],max_source_area_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

axs[0][4].scatter(total_migration_duration[0],max_source_area[0], c=distances[0], cmap="Blues")
axs[0][5].scatter(total_migration_duration[1],max_source_area[1], c=distances[0], cmap="Blues")

axs[1][4].scatter(total_migration_duration[0],average_source_area[0], c=distances[0], cmap="Greens")
axs[1][5].scatter(total_migration_duration[1],average_source_area[1], c=distances[1], cmap="Greens")

axs[2][4].scatter(total_migration_duration[0],max_source_area_R[0], c=distances[0], cmap="Grays", label="R", s=40, marker="s")
axs[2][5].scatter(total_migration_duration[1],max_source_area_R[1], c=distances[1], cmap="Grays", label="R", s=40, marker="s")
axs[2][4].scatter(total_migration_duration[0],max_source_area_L[0], c=distances[1], cmap="Grays", label="L", s=60, marker="o")
axs[2][5].scatter(total_migration_duration[1],max_source_area_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

axs[0][6].scatter(total_migration_start[0],max_source_area[0], c=distances[0], cmap="Blues")
axs[0][7].scatter(total_migration_start[1],max_source_area[1], c=distances[0], cmap="Blues")

axs[1][6].scatter(total_migration_start[0],average_source_area[0], c=distances[0], cmap="Greens")
axs[1][7].scatter(total_migration_start[1],average_source_area[1], c=distances[1], cmap="Greens")

axs[2][6].scatter(total_migration_start[0],max_source_area_R[0], c=distances[0], cmap="Grays", label="R", s=40, marker="s")
axs[2][7].scatter(total_migration_start[1],max_source_area_R[1], c=distances[1], cmap="Grays", label="R", s=40, marker="s")
axs[2][6].scatter(total_migration_start[0],max_source_area_L[0], c=distances[1], cmap="Grays", label="L", s=60, marker="o")
axs[2][7].scatter(total_migration_start[1],max_source_area_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

# Ranges and labels of the axes
craton_distance_labels = ["50", "100", "150", r"$\infty$"]
ftsize = 7
axs[0][0].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs[0][1].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs[0][2].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs[0][3].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs[0][4].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs[0][5].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs[0][6].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs[0][7].set_title("Wide",weight="bold",fontsize=ftsize+2)

axs[0][0].set_ylabel("Av. max source area [km2]",weight="bold",fontsize=ftsize+2)
axs[0][0].set_yticks([0,10,20,30,40])
axs[0][0].set_yticklabels(["0","10","20","30","40"],fontsize=ftsize)
axs[1][0].set_ylabel("Av. av. source area [km2]",weight="bold",fontsize=ftsize+2)
axs[1][0].set_yticks([0,4,8,12])
axs[1][0].set_yticklabels(["0","4","8","12"],fontsize=ftsize)
axs[2][0].set_ylabel("Av. max source area [km2]",weight="bold",fontsize=ftsize+2)
axs[2][0].set_yticks([0,10,20,30,40,50])
axs[2][0].set_yticklabels(["0","10","20","30","40","50"],fontsize=ftsize)

axs[2][0].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs[2][0].set_xticks([50,100,150,200])
axs[2][0].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)
axs[2][1].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs[2][1].set_xticks([50,100,150,200])
axs[2][1].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)

axs[2][2].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs[2][2].set_xticks([5,10,15,20])
axs[2][2].set_xticklabels(["5","10","15","20"],fontsize=ftsize)
axs[2][3].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs[2][3].set_xticks([15,17.5,20])
axs[2][3].set_xticklabels(["15","17.5","20"],fontsize=ftsize)

axs[2][4].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs[2][4].set_xticks([10,12.5,15])
axs[2][4].set_xticklabels(["10","12.5","15"],fontsize=ftsize)
axs[2][5].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs[2][5].set_xticks([5,7.5,10])
axs[2][5].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs[n_rows-1][6].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs[n_rows-1][6].set_xticks([5,10,15])
axs[n_rows-1][6].set_xticklabels(["5","10","15"],fontsize=ftsize)
axs[n_rows-1][7].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs[n_rows-1][7].set_xticks([5,7.5,10])
axs[n_rows-1][7].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs[2][0].legend(loc='lower right',ncol=1,handlelength=1,fontsize=ftsize)
axs[2][1].legend(loc='upper right',ncol=1,handlelength=1,fontsize=ftsize)

## Save figure
plt.savefig(output_name + 'source_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + 'source_CERI_cratons.png')

## Create empty plot for OFMs
n_columns2 = 8
n_rows2 = 4
fig2, axs2 = plt.subplots(n_rows2,n_columns2,figsize=(2*n_columns2, 2*n_rows2),dpi=300, sharex='col', sharey='row')
fig2.subplots_adjust(hspace = 0.05)
fig2.subplots_adjust(wspace = 0.05)

## Plot the average total OFMs and OFM1s per suite
axs2[0][0].scatter(distances[0],total_OFMs_R[0], c=distances[0], cmap="Greens", label="OFMs R", s=40, marker="s")
axs2[0][1].scatter(distances[1],total_OFMs_R[1], c=distances[1], cmap="Greens", label="OFMs R", s=40, marker="s")
axs2[0][0].scatter(distances[0],total_OFMs_L[0], c=distances[0], cmap="Greys", label="OFMs L", s=40, marker="o")
axs2[0][1].scatter(distances[1],total_OFMs_L[1], c=distances[1], cmap="Greys", label="OFMs L", s=40, marker="o")
axs2[0][0].scatter(distances[0],total_OFMs[0], c=distances[0], cmap="Blues", label="OFMs", s=60, marker="v")
axs2[0][1].scatter(distances[1],total_OFMs[1], c=distances[1], cmap="Blues", label="OFMs", s=60, marker="v")

axs2[1][0].scatter(distances[0],total_OFM1s[0], c=distances[0], cmap="Greens", label="OFM1s")
axs2[1][1].scatter(distances[1],total_OFM1s[1], c=distances[1], cmap="Greens", label="OFM1s")
axs2[1][0].scatter(distances[0],total_OFM2s[0], c=distances[0], cmap="Greys", label="OFM2s")
axs2[1][1].scatter(distances[1],total_OFM2s[1], c=distances[1], cmap="Greys", label="OFM2s")

axs2[2][0].scatter(distances[0],total_OFM12s_R[0], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s")
axs2[2][1].scatter(distances[1],total_OFM12s_R[1], c=distances[1], cmap="Greens", label="OFM12s R", s=40, marker="s")
axs2[2][0].scatter(distances[0],total_OFM12s_L[0], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o")
axs2[2][1].scatter(distances[1],total_OFM12s_L[1], c=distances[1], cmap="Greys", label="OFM12s L", s=40, marker="o")
axs2[2][0].scatter(distances[0],total_OFM12s[0], c=distances[0], cmap="Blues", label="OFM12s", s=60, marker="v")
axs2[2][1].scatter(distances[1],total_OFM12s[1], c=distances[1], cmap="Blues", label="OFM12s", s=60, marker="v")

axs2[3][0].scatter(distances[0],total_timesteps_OFM12s_R[0], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][1].scatter(distances[1],total_timesteps_OFM12s_R[1], c=distances[1], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][0].scatter(distances[0],total_timesteps_OFM12s_L[0], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][1].scatter(distances[1],total_timesteps_OFM12s_L[1], c=distances[1], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][0].scatter(distances[0],total_timesteps_OFM12s[0], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][1].scatter(distances[1],total_timesteps_OFM12s[1], c=distances[1], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][0].scatter(distances[0],total_timesteps_OFMs[0], c=distances[0], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)
axs2[3][1].scatter(distances[1],total_timesteps_OFMs[1], c=distances[1], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)

axs2[0][2].scatter(total_border_fault_duration[0],total_OFMs[0], c=distances[0], cmap="Blues")
axs2[0][3].scatter(total_border_fault_duration[1],total_OFMs[1], c=distances[1], cmap="Blues")

axs2[1][2].scatter(total_border_fault_duration[0],total_OFM1s[0], c=distances[0], cmap="Greens")
axs2[1][3].scatter(total_border_fault_duration[1],total_OFM1s[1], c=distances[1], cmap="Greens")
axs2[1][2].scatter(total_border_fault_duration[0],total_OFM2s[0], c=distances[0], cmap="Greys")
axs2[1][3].scatter(total_border_fault_duration[1],total_OFM2s[1], c=distances[1], cmap="Greys")

axs2[2][2].scatter(total_border_fault_duration[0],total_OFM12s_R[0], c=distances[0], cmap="Greens", label="R", s=40, marker="s")
axs2[2][3].scatter(total_border_fault_duration[1],total_OFM12s_R[1], c=distances[1], cmap="Greens", label="R", s=40, marker="s")
axs2[2][2].scatter(total_border_fault_duration[0],total_OFM12s_L[0], c=distances[0], cmap="Grays", label="L", s=60, marker="o")
axs2[2][3].scatter(total_border_fault_duration[1],total_OFM12s_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

axs2[3][2].scatter(total_border_fault_duration[0],total_timesteps_OFM12s_R[0], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][3].scatter(total_border_fault_duration[1],total_timesteps_OFM12s_R[1], c=distances[1], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][2].scatter(total_border_fault_duration[0],total_timesteps_OFM12s_L[0], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][3].scatter(total_border_fault_duration[1],total_timesteps_OFM12s_L[1], c=distances[1], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][2].scatter(total_border_fault_duration[0],total_timesteps_OFM12s[0], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][3].scatter(total_border_fault_duration[1],total_timesteps_OFM12s[1], c=distances[1], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][2].scatter(total_border_fault_duration[0],total_timesteps_OFMs[0], c=distances[0], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)
axs2[3][3].scatter(total_border_fault_duration[1],total_timesteps_OFMs[1], c=distances[1], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)

axs2[0][4].scatter(total_migration_duration[0],total_OFMs[0], c=distances[0], cmap="Blues")
axs2[0][5].scatter(total_migration_duration[1],total_OFMs[1], c=distances[1], cmap="Blues")

axs2[1][4].scatter(total_migration_duration[0],total_OFM1s[0], c=distances[0], cmap="Greens")
axs2[1][5].scatter(total_migration_duration[1],total_OFM1s[1], c=distances[1], cmap="Greens")
axs2[1][4].scatter(total_migration_duration[0],total_OFM2s[0], c=distances[0], cmap="Greys")
axs2[1][5].scatter(total_migration_duration[1],total_OFM2s[1], c=distances[1], cmap="Greys")

axs2[2][4].scatter(total_migration_duration[0],total_OFM12s_R[0], c=distances[0], cmap="Greens", label="R", s=40, marker="s")
axs2[2][5].scatter(total_migration_duration[1],total_OFM12s_R[1], c=distances[1], cmap="Greens", label="R", s=40, marker="s")
axs2[2][4].scatter(total_migration_duration[0],total_OFM12s_L[0], c=distances[0], cmap="Grays", label="L", s=60, marker="o")
axs2[2][5].scatter(total_migration_duration[1],total_OFM12s_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")

axs2[3][4].scatter(total_migration_duration[0],total_timesteps_OFM12s_R[0], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][5].scatter(total_migration_duration[1],total_timesteps_OFM12s_R[1], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][4].scatter(total_migration_duration[0],total_timesteps_OFM12s_L[0], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][5].scatter(total_migration_duration[1],total_timesteps_OFM12s_L[1], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][4].scatter(total_migration_duration[0],total_timesteps_OFM12s[0], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][5].scatter(total_migration_duration[1],total_timesteps_OFM12s[1], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][4].scatter(total_migration_duration[0],total_timesteps_OFMs[0], c=distances[0], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)
axs2[3][5].scatter(total_migration_duration[1],total_timesteps_OFMs[1], c=distances[1], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)

axs2[0][6].scatter(total_migration_start[0],total_OFMs[0], c=distances[0], cmap="Blues")
axs2[0][7].scatter(total_migration_start[1],total_OFMs[1], c=distances[0], cmap="Blues")

axs2[1][6].scatter(total_migration_start[0],total_OFM1s[0], c=distances[0], cmap="Greens")
axs2[1][7].scatter(total_migration_start[1],total_OFM1s[1], c=distances[1], cmap="Greens")
axs2[1][6].scatter(total_migration_start[0],total_OFM2s[0], c=distances[0], cmap="Greys")
axs2[1][7].scatter(total_migration_start[1],total_OFM2s[1], c=distances[1], cmap="Greys")

axs2[2][6].scatter(total_migration_start[0],total_OFM12s_R[0], c=distances[0], cmap="Greens", label="R", s=40, marker="s")
axs2[2][7].scatter(total_migration_start[1],total_OFM12s_R[1], c=distances[1], cmap="Greens", label="R", s=40, marker="s")
axs2[2][6].scatter(total_migration_start[0],total_OFM12s_L[0], c=distances[1], cmap="Grays", label="L", s=60, marker="o")
axs2[2][7].scatter(total_migration_start[1],total_OFM12s_L[1], c=distances[1], cmap="Grays", label="L", s=60, marker="o")


axs2[3][6].scatter(total_migration_start[0],total_timesteps_OFM12s_R[0], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][7].scatter(total_migration_start[1],total_timesteps_OFM12s_R[1], c=distances[0], cmap="Greens", label="OFM12s R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs2[3][6].scatter(total_migration_start[0],total_timesteps_OFM12s_L[0], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][7].scatter(total_migration_start[1],total_timesteps_OFM12s_L[1], c=distances[0], cmap="Greys", label="OFM12s L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs2[3][6].scatter(total_migration_start[0],total_timesteps_OFM12s[0], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][7].scatter(total_migration_start[1],total_timesteps_OFM12s[1], c=distances[0], cmap="Purples", label="OFM12s", s=40, marker="v",edgecolors='black',linewidths=0.5)
axs2[3][6].scatter(total_migration_start[0],total_timesteps_OFMs[0], c=distances[0], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)
axs2[3][7].scatter(total_migration_start[1],total_timesteps_OFMs[1], c=distances[1], cmap="Blues", label="OFMs", s=60, marker="*",edgecolors='black',linewidths=0.5)

# Ranges and labels of the axes
axs2[0][0].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs2[0][1].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs2[0][2].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs2[0][3].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs2[0][4].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs2[0][5].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs2[0][6].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs2[0][7].set_title("Wide",weight="bold",fontsize=ftsize+2)

axs2[0][0].set_ylabel("Av. total OFMs",weight="bold",fontsize=ftsize+2)
axs2[0][0].set_yticks([0,10,20,30,40])
axs2[0][0].set_yticklabels(["0","10","20","30","40"],fontsize=ftsize)
axs2[1][0].set_ylabel("Av. total OFM1/2s",weight="bold",fontsize=ftsize+2)
axs2[1][0].set_yticks([0,4,8,12,16])
axs2[1][0].set_yticklabels(["0","4","8","12","16"],fontsize=ftsize)
axs2[2][0].set_ylabel("Av. total OFM12s",weight="bold",fontsize=ftsize+2)
axs2[2][0].set_yticks([0,4,8,12,16,20,24])
axs2[2][0].set_yticklabels(["0","4","8","12","16","20","24"],fontsize=ftsize)
axs2[3][0].set_ylabel("Av. timesteps with OFMs",weight="bold",fontsize=ftsize+2)
axs2[3][0].set_yticks([0,5,10,15,20,25])
axs2[3][0].set_yticklabels(["0","5","10","15","20","25"],fontsize=ftsize)

axs2[3][0].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs2[3][0].set_xticks([50,100,150,200])
axs2[3][0].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)
axs2[3][1].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs2[3][1].set_xticks([50,100,150,200])
axs2[3][1].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)

axs2[3][2].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs2[3][2].set_xticks([5,10,15,20])
axs2[3][2].set_xticklabels(["5","10","15","20"],fontsize=ftsize)
axs2[3][3].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs2[3][3].set_xticks([15,17.5,20])
axs2[3][3].set_xticklabels(["15","17.5","20"],fontsize=ftsize)

axs2[3][4].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs2[3][4].set_xticks([10,12.5,15])
axs2[3][4].set_xticklabels(["10","12.5","15"],fontsize=ftsize)
axs2[3][5].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs2[3][5].set_xticks([5,7.5,10])
axs2[3][5].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs2[n_rows2-1][6].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs2[n_rows2-1][6].set_xticks([5,10,15])
axs2[n_rows2-1][6].set_xticklabels(["5","10","15"],fontsize=ftsize)
axs2[n_rows2-1][7].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs2[n_rows2-1][7].set_xticks([5,7.5,10])
axs2[n_rows2-1][7].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs2[0][0].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[0][1].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[1][0].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[1][1].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[2][0].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[2][1].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[3][0].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)
axs2[3][1].legend(loc='upper right',ncol=1,handlelength=0.8,fontsize=ftsize-2)

## Save figure
plt.savefig(output_name + 'OFM_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + 'OFM_CERI_cratons.png')

## Create empty plot for number of source areas
n_columns3 = 8
n_rows3 = 2
fig3, axs3 = plt.subplots(n_rows3,n_columns3,figsize=(2*n_columns3, 2*n_rows3),dpi=300, sharex='col', sharey='row')
fig3.subplots_adjust(hspace = 0.05)
fig3.subplots_adjust(wspace = 0.05)

## Plot the average max and average source area per suite total OFMs and OFM1s per suite
axs3[0][0].scatter(distances[0],total_max_nr_source_R[0], c=distances[0], cmap="Greens", label="R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs3[0][1].scatter(distances[1],total_max_nr_source_R[1], c=distances[1], cmap="Greens", label="R", s=40, marker="s",edgecolors='black',linewidths=0.5)
axs3[0][0].scatter(distances[0],total_max_nr_source_L[0], c=distances[0], cmap="Greys", label="L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs3[0][1].scatter(distances[1],total_max_nr_source_L[1], c=distances[1], cmap="Greys", label="L", s=40, marker="o",edgecolors='black',linewidths=0.5)
axs3[0][0].scatter(distances[0],total_max_nr_source[0], c=distances[0], cmap="Blues", label="Total", s=60, marker="v",edgecolors='black',linewidths=0.5)
axs3[0][1].scatter(distances[1],total_max_nr_source[1], c=distances[1], cmap="Blues", label="Total", s=60, marker="v",edgecolors='black',linewidths=0.5)

axs3[1][0].scatter(distances[0],total_nr_source[0], c=distances[0], cmap="Greens")
axs3[1][1].scatter(distances[1],total_nr_source[1], c=distances[1], cmap="Greens")

axs3[0][2].scatter(total_border_fault_duration[0],total_max_nr_source[0], c=distances[0], cmap="Blues")
axs3[0][3].scatter(total_border_fault_duration[1],total_max_nr_source[1], c=distances[1], cmap="Blues")
axs3[1][2].scatter(total_border_fault_duration[0],total_nr_source[0], c=distances[0], cmap="Greens")
axs3[1][3].scatter(total_border_fault_duration[1],total_nr_source[1], c=distances[1], cmap="Greens")

axs3[0][4].scatter(total_migration_duration[0],total_max_nr_source[0], c=distances[0], cmap="Blues")
axs3[0][5].scatter(total_migration_duration[1],total_max_nr_source[1], c=distances[0], cmap="Blues")
axs3[1][4].scatter(total_migration_duration[0],total_nr_source[0], c=distances[0], cmap="Greens")
axs3[1][5].scatter(total_migration_duration[1],total_nr_source[1], c=distances[0], cmap="Greens")

axs3[0][6].scatter(total_migration_start[0],total_max_nr_source[0], c=distances[0], cmap="Blues")
axs3[0][7].scatter(total_migration_start[1],total_max_nr_source[1], c=distances[0], cmap="Blues")
axs3[1][6].scatter(total_migration_start[0],total_nr_source[0], c=distances[0], cmap="Greens")
axs3[1][7].scatter(total_migration_start[1],total_nr_source[1], c=distances[0], cmap="Greens")

# Ranges and labels of the axes
axs3[0][0].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs3[0][1].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs3[0][2].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs3[0][3].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs3[0][4].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs3[0][5].set_title("Wide",weight="bold",fontsize=ftsize+2)
axs3[0][6].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs3[0][7].set_title("Wide",weight="bold",fontsize=ftsize+2)

axs3[0][0].set_ylabel("Av. max nr of source areas [-]",weight="bold",fontsize=ftsize+2)
axs3[0][0].set_yticks([0,2,4,6,8,10])
axs3[0][0].set_yticklabels(["0","2","4","6","8","10"],fontsize=ftsize)

axs3[1][0].set_ylabel("Av. nr of source areas [-]",weight="bold",fontsize=ftsize+2)
axs3[1][0].set_yticks([0,20,40,60,80])
axs3[1][0].set_yticklabels(["0","20","40","60","80"],fontsize=ftsize)
# axs3[2][0].set_ylabel("Av. max source area [km2]",weight="bold",fontsize=ftsize+2)
# axs3[2][0].set_yticks([0,10,20,30,40,50])
# axs3[2][0].set_yticklabels(["0","10","20","30","40","50"],fontsize=ftsize)

axs3[n_rows3-1][0].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][0].set_xticks([50,100,150,200])
axs3[n_rows3-1][0].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)
axs3[n_rows3-1][1].set_xlabel("Craton edge distance [km]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][1].set_xticks([50,100,150,200])
axs3[n_rows3-1][1].set_xticklabels(["50","100","150","inf"],fontsize=ftsize)

axs3[n_rows3-1][2].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][2].set_xticks([5,10,15,20])
axs3[n_rows3-1][2].set_xticklabels(["5","10","15","20"],fontsize=ftsize)
axs3[n_rows3-1][3].set_xlabel("Border fault duration [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][3].set_xticks([15,17.5,20])
axs3[n_rows3-1][3].set_xticklabels(["15","17.5","20"],fontsize=ftsize)

axs3[n_rows3-1][4].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][4].set_xticks([10,12.5,15])
axs3[n_rows3-1][4].set_xticklabels(["10","12.5","15"],fontsize=ftsize)
axs3[n_rows3-1][5].set_xlabel("Migration duration [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][5].set_xticks([5,7.5,10])
axs3[n_rows3-1][5].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs3[n_rows3-1][6].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][6].set_xticks([5,10,15])
axs3[n_rows3-1][6].set_xticklabels(["5","10","15"],fontsize=ftsize)
axs3[n_rows3-1][7].set_xlabel("Migration start [My]",weight="bold",fontsize=ftsize+2)
axs3[n_rows3-1][7].set_xticks([5,7.5,10])
axs3[n_rows3-1][7].set_xticklabels(["5","7.5","10"],fontsize=ftsize)

axs3[0][0].legend(loc='lower right',ncol=1,handlelength=1,fontsize=ftsize)
# axs3[0][1].legend(loc='upper right',ncol=1,handlelength=1,fontsize=ftsize)

## Save figure
plt.savefig(output_name + 'nr_source_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + 'nr_source_CERI_cratons.png')

## Create empty plot to plot against migration direction
n_columns4 = 2
n_rows4 = 5
fig4, axs4 = plt.subplots(n_rows4,n_columns4,figsize=(2*n_columns4, 2*n_rows4),dpi=300, sharex='col', sharey='row')
fig4.subplots_adjust(hspace = 0.05)
fig4.subplots_adjust(wspace = 0.05)

axs4[0][0].scatter(0,n_OFMs_R[0], color="green", label="R", s=40, marker="s")
axs4[0][1].scatter(0,n_OFMs_R[1], color="green", label="R", s=40, marker="s")
axs4[0][0].scatter(1,n_OFMs_L[0], color="grey", label="L", s=40, marker="o")
axs4[0][1].scatter(1,n_OFMs_L[1], color="grey", label="L", s=40, marker="o")

axs4[1][0].scatter(0,n_OFM12s_R[0], color="green", label="R", s=40, marker="s")
axs4[1][1].scatter(0,n_OFM12s_R[1], color="green", label="R", s=40, marker="s")
axs4[1][0].scatter(1,n_OFM12s_L[0], color="grey", label="L", s=40, marker="o")
axs4[1][1].scatter(1,n_OFM12s_L[1], color="grey", label="L", s=40, marker="o")

axs4[2][0].scatter(0,n_timesteps_OFM12s_R[0], color="green", label="R", s=40, marker="s")
axs4[2][1].scatter(0,n_timesteps_OFM12s_R[1], color="green", label="R", s=40, marker="s")
axs4[2][0].scatter(1,n_timesteps_OFM12s_L[0], color="grey", label="L", s=40, marker="o")
axs4[2][1].scatter(1,n_timesteps_OFM12s_L[1], color="grey", label="L", s=40, marker="o")

axs4[3][0].scatter(0,n_max_source_area_R[0], color="green", label="R", s=40, marker="s")
axs4[3][1].scatter(0,n_max_source_area_R[1], color="green", label="R", s=40, marker="s")
axs4[3][0].scatter(1,n_max_source_area_L[0], color="grey", label="L", s=40, marker="o")
axs4[3][1].scatter(1,n_max_source_area_L[1], color="grey", label="L", s=40, marker="o")

axs4[4][0].scatter(0,n_max_nr_source_R[0], color="green", label="R", s=40, marker="s")
axs4[4][1].scatter(0,n_max_nr_source_R[1], color="green", label="R", s=40, marker="s")
axs4[4][0].scatter(1,n_max_nr_source_L[0], color="grey", label="L", s=40, marker="o")
axs4[4][1].scatter(1,n_max_nr_source_L[1], color="grey", label="L", s=40, marker="o")

# Ranges and labels of the axes
axs4[0][0].set_title("Narrow asymmetric",weight="bold",fontsize=ftsize+2)
axs4[0][1].set_title("Wide",weight="bold",fontsize=ftsize+2)

axs4[0][0].set_ylabel("Av. total OFMs",weight="bold",fontsize=ftsize+2)
axs4[0][0].set_yticks([0,10,20,30,40])
axs4[0][0].set_yticklabels(["0","10","20","30","40"],fontsize=ftsize)

axs4[1][0].set_ylabel("Av. total OFM12s",weight="bold",fontsize=ftsize+2)
axs4[1][0].set_yticks([0,4,8,12,16,20,24])
axs4[1][0].set_yticklabels(["0","4","8","12","16","20","24"],fontsize=ftsize)

axs4[2][0].set_ylabel("Av. timesteps with OFM12s",weight="bold",fontsize=ftsize+2)
axs4[2][0].set_yticks([0,5,10,15])
axs4[2][0].set_yticklabels(["0","5","10","15"],fontsize=ftsize)

axs4[3][0].set_ylabel("Av. max source area [km2]",weight="bold",fontsize=ftsize+2)
axs4[3][0].set_yticks([0,10,20,30,40])
axs4[3][0].set_yticklabels(["0","10","20","30","40"],fontsize=ftsize)

axs4[4][0].set_ylabel("Av. max nr source areas [-]",weight="bold",fontsize=ftsize+2)
axs4[4][0].set_yticks([0,2,4,6,8])
axs4[4][0].set_yticklabels(["0","2","4","6","8"],fontsize=ftsize)

axs4[n_rows4-1][0].legend(loc='lower right',ncol=1,handlelength=1,fontsize=ftsize)
axs4[n_rows4-1][0].set_xlabel("Migration direction",weight="bold",fontsize=ftsize+2)
axs4[n_rows4-1][1].set_xlabel("Migration direction",weight="bold",fontsize=ftsize+2)

## Save figure
plt.savefig(output_name + 'migration_direction_CERI_cratons.png',dpi=300)    
print ("Figure in: ", output_name + 'migration_direction_CERI_cratons.png')

##### SAVE #####
## Print and save the data
#print ("Average total OFMs: ", total_OFMs)
#print ("Average total OFM1s: ", total_OFM1s)
#print ("Average total OFM2s: ", total_OFM2s)
#print ("Average total timesteps with OFM12s: ", total_timesteps_OFM12s)
#print ("Average total timesteps with OFMs: ", total_timesteps_OFMs)
# Data order:
# NA-50km
# NA-100km
# NA-150km
# NA-inf
# W-50km
# W-100km
# W-150km
# W-inf
# total_OFMs.tofile(output_name + '_average_total_OFMs_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFMs_CERI_cratons.csv')
# total_OFM1s.tofile(output_name + '_average_total_OFM1s_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFM1s_CERI_cratons.csv')
# total_OFM2s.tofile(output_name + '_average_total_OFM2s_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFM2s_CERI_cratons.csv')
# total_OFM12s.tofile(output_name + '_average_total_OFM12s_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFM12s_CERI_cratons.csv')
# total_OFM12s_R.tofile(output_name + '_average_total_OFM12s_R_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFM12s_R_CERI_cratons.csv')
# total_OFM12s_L.tofile(output_name + '_average_total_OFM12s_L_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_OFM12s_L_CERI_cratons.csv')
# total_timesteps_OFM12s_R.tofile(output_name + '_average_total_timesteps_OFM12s_R_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_timesteps_OFM12s_R_CERI_cratons.csv')
# total_timesteps_OFM12s_L.tofile(output_name + '_average_total_timesteps_OFM12s_L_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_timesteps_OFM12s_L_CERI_cratons.csv')
# total_timesteps_OFM12s.tofile(output_name + '_average_total_timesteps_OFM12s_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_timesteps_OFM12s_CERI_cratons.csv')
# total_timesteps_OFMs.tofile(output_name + '_average_total_timesteps_OFMs_CERI_cratons.csv', sep=' ')
# print ("Data in: ", output_name + '_average_total_timesteps_OFMs_CERI_cratons.csv')