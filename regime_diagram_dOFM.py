# -*- coding: utf-8 -*-
"""
Created on Mon 20 Jan 2024 by Anne Glerum
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
print ("Seaborn version: ", sns.__version__)
print ("Pandas version: ", pd.__version__)
print ("Matplotlib version: ", matplotlib.__version__)

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

output_name = '5p_fixed_regime_diagram_dOFM_craton400km_cuttonewOS_test'

# File name
# real file
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.csv"
tail = r"5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_cuttonewOS.csv"

###### Model names ######
model_index = 8
models = [
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
]
# Structure of input file: 3x9 rows of the following columns:
# initial_craton_distance,initial_fault_geometry,start_left_border_fault,start_right_border_fault,end_left_border_fault,end_right_border_fault,start_migration,end_migration,migration_direction,start_oceanic_spreading,n_source_max,n_source_host_max,n_OFM3_max,n_OFM1_max,n_OFM2_max,n_OFM12_max
columns_to_plot = ['time', 'time']
rows_to_plot = ['n_OFM3', 'n_OFM2', 'n_OFM1']

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

# Add index column
#dataframe['index'] = dataframe[

# Check data
#print ("Interpretation data file: ", dataframe.dtypes)
#if not set(columns_to_plot).issubset(dataframe.columns):
#  exit("The requested data columns are not available, exiting.")
if not set(["n_OFM3_max","n_OFM2_max","n_OFM1_max","n_source_max","source_max"]).issubset(dataframe.columns):
  exit("The requested data columns are not available, exiting.")

# The runs without a craton have an artificial craton distance of 2000 km. Replace this value
# with 550 km, but label axis as "infinite".
dataframe.loc[dataframe['initial_craton_distance'] == 2000, 'initial_craton_distance'] = 550

# Order of initial geometries
# 5p
#order_geometries = ["Lside-ULCshear Lside-Rdip",
#"ULCshear-LD Lside-Rdip",
#"ULCshear 2Lside-Rdip",
#"ULCshear Lside-Rdip",
#"ULCshear Lside-Rdip Rside-Ldip",
#"ULCshear Rside-Ldip-D Lside-Rdip",
#"ULCshear Lside-Rdip 2Rside-Ldip",
#"ULCshear Rside-Ldip"]
# 5o
order_geometries = [
"Lside-ULCshear 2Lside-Rdip", #
"Lside-ULCshear Lside-C Lside-Rdip", #
"Lside-ULCshear Lside-Rdip",#
"Lside-ULCshear",#
"ULCshear-LD Lside-Rdip",#
"ULCshear 3Lside-Rdip",
"ULCshear 2Lside-Rdip",
"ULCshear Lside-C",#
"ULCshear Lside-Rdip", #
"ULCshear 2Lside-Rdip Rside-Ldip",#
"ULCshear Lside-C Rside-Ldip",#
"ULCshear Lside-C 2Rside-Ldip",#
"ULCshear Lside-Rdip Rside-Ldip",#
"ULCshear Lside-Ldip Rside-Ldip",#
"ULCshear Lside-Rdip 2Rside-Ldip",#
"ULCshear Rside-Ldip",#
"ULCshear 2Rside-Ldip"]#

dataframe.initial_fault_geometry = dataframe.initial_fault_geometry.astype("category")
dataframe.initial_fault_geometry = dataframe.initial_fault_geometry.cat.set_categories(order_geometries)
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
fig, axs = plt.subplots(n_rows,n_columns,figsize=(2*n_columns, 2*n_rows),dpi=300, sharex='col', sharey='row')
#fig.subplots_adjust(left = 0.2)

#print (sns.color_palette())
#[(0.2980392156862745, 0.4470588235294118, 0.6901960784313725), 
# (0.8666666666666667, 0.5176470588235295, 0.3215686274509804),
# (0.3333333333333333, 0.6588235294117647, 0.40784313725490196),
# (0.7686274509803922, 0.3058823529411765, 0.3215686274509804),
# (0.5058823529411764, 0.4470588235294118, 0.7019607843137254),
# (0.5764705882352941, 0.47058823529411764, 0.3764705882352941),
# etc

# Regression confidence interval
confidence_interval = 0
# Which markers for which migration direction
markers = {'L': 'o', 'C':'X', 'R': 's'}
# Order in which style and hue are applied according to migration direction
order = ["L", "C", "R"]
# Repeated parameters for regression
reg_prms = {"scatter":False,"robust":False,"order":1,"ci":confidence_interval}

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

###### Create file paths ######
paths = [base+m for m in models]
ASPECT_time_steps = ['00000','00001','00002','00003','00004','00005','00006','00007','00008','00009','00010','00011','00012','00013','00014','00015','00016','00017','00018','00019','00020','00021','00022','00023','00024','00025','00026','00027','00028','00029','00030','00031','00032','00033','00034','00035','00036','00037','00038','00039','00040','00041','00042','00043','00044','00045','00046','00047','00048','00049','00050']

###### Loop over requested models ######
for m in models:

  if Path(m).exists():
    path = base + m
    stat_files = sorted(Path(path).glob('*stats_2*'))
  if len(stat_files) == 1:
    # Read the data file
    filename = m + "/" + stat_files[0].name
    dataframe_stats = pd.read_csv(filename, sep=",") #,converters={'time': int,'n_OFM1': int,'n_OFM2': int, 'n_OFM3': int})
    if "craton400" in m:
      dataframe_stats['initial_craton_distance'] = 400
      print ("400")
    elif "craton450" in m:
      dataframe_stats['initial_craton_distance'] = 450
      print ("450")
    elif "craton500" in m:
      dataframe_stats['initial_craton_distance'] = 500
      print ("500")
    else:
      dataframe_stats['initial_craton_distance'] = 2000
    dataframe_stats['time'] = dataframe_stats['time'].div(2)
    dataframe_stats['n_OFM12'] = dataframe_stats['n_OFM1'] + dataframe_stats['n_OFM2']
    dataframe_stats = dataframe_stats.assign(**{"index": counter})

    df_stats_n_OFM1 = dataframe_stats.copy()
    df_stats_n_OFM1 = df_stats_n_OFM1[df_stats_n_OFM1["n_OFM1"] > 0]
    df_stats_n_OFM1['type_OFM'] = 'OFM1'
    
    df_stats_n_OFM2 = dataframe_stats.copy()
    df_stats_n_OFM2 = df_stats_n_OFM2[df_stats_n_OFM2["n_OFM2"] > 0]
    df_stats_n_OFM2['type_OFM'] = 'OFM2'
    
    df_stats_n_OFM3 = dataframe_stats.copy()
    df_stats_n_OFM3 = df_stats_n_OFM3[df_stats_n_OFM3["n_OFM3"] > 0]
    df_stats_n_OFM3['type_OFM'] = 'OFM3'

    # Plot OFMs over time
    sns.stripplot(data=df_stats_n_OFM3,x="time",y="type_OFM",ax=axs[2,0],hue="n_OFM3",palette=palette_n_OFM,legend=False)
    sns.stripplot(data=df_stats_n_OFM2,x="time",y="type_OFM",ax=axs[2,0],hue="n_OFM2",palette=palette_n_OFM,legend=False)
    sns.stripplot(data=df_stats_n_OFM1,x="time",y="type_OFM",ax=axs[2,0],hue="n_OFM1",palette=palette_n_OFM,legend=True)

    counter += 1

  else:
    print ("Multiple or no summary files for model: ", m)

  # Plot
  dataframe_model = dataframe.iloc[model_index]
  border_fault_data = {'LBF': [dataframe_model['start_left_border_fault'],dataframe_model['end_left_border_fault']]}
  df_model_border_faults = pd.DataFrame(border_fault_data)
  #sns.scatterplot(data=dataframe_model,x="time",y="n_OFM3",ax=axs[0,0],hue="index",palette=palette_n_OFM,legend=False) #,size="n_OFM12",sizes=(0,200))
  #sns.scatterplot(data=dataframe_model,x="time",y="n_OFM2",ax=axs[1,0],hue="index",palette=palette_n_OFM,legend=False) #,size="n_OFM12",sizes=(0,200))


# Ranges and labels of the axes
# TODO Would be great not to repeat this for both the x and y axis.
ftsize = 6
craton_distance_labels = ["50", "100", "150", r"$\infty$"]
#5p
#initial_geometry_labels = ["L-ULC L-Rdip", "ULC-LD L-Rdip", "ULC 2L-Rdip", "ULC L-Rdip", "ULC L-Rdip R-Ldip", "ULC L-Rdip R-Ldip-D", "ULC L-Rdip 2R-Ldip","ULC R-Ldip"]
#5o
initial_geometry_labels = [
"L-ULC 2L-Rdip",
"L-ULC L-C L-Rdip",
"L-ULC L-Rdip",
"L-ULC",
"ULC-LD L-Rdip",#
"ULC 3L-Rdip",
"ULC 2L-Rdip",
"ULC L-C",#
"ULC L-Rdip", #
"ULC 2L-Rdip R-Ldip",#
"ULC L-C R-Ldip",#
"ULC L-C 2R-Ldip",#
"ULC L-Rdip R-Ldip",#
"ULC L-Ldip R-Ldip",#
"ULC L-Rdip 2R-Ldip",#
"ULC R-Ldip",
"ULC 2R-Ldip"]
# 5o
migration_duration_min = 2
migration_duration_max = 14
migration_duration_ticks = [2,6,10,14.0]
LBF_duration_min = 7
LBF_duration_max = 22
LBF_duration_ticks = [7,12,17,22]
RBF_duration_min = 2
RBF_duration_max = 22
RBF_duration_ticks = [2,7,12,17,22]

# 5p
# migration_duration_min = 5
# migration_duration_max = 20
# migration_duration_ticks = [5.0,10.0,15.0,20.0]
# LBF_duration_min = 0
# LBF_duration_max = 25
# LBF_duration_ticks = [0,5,10,15,20,25]
# RBF_duration_min = 2
# RBF_duration_max = 22
# RBF_duration_ticks = [2.0,7,12,17,22]
OFM12_max = 5
for ax in axs.reshape(-1):
  if ax.get_xlabel() == 'initial_craton_distance':
    ax.set_xlim(350,600) # km
    ax.set_xticks([400,450,500,550])
    ax.set_xticklabels(craton_distance_labels)
    ax.set_xlabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'initial_fault_geometry':
    ax.tick_params(axis='x', labelrotation=90,labelsize=3)
    ax.set_xticks(order_geometries)
    ax.set_xticklabels(initial_geometry_labels)
    ax.set_xlabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_migration':
    ax.set_xlim(5,10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'migration_direction':
    ax.margins(x=0.2)
    ax.set_xlabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_left_border_fault':
    ax.set_xlim(0,10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'start_right_border_fault':
    ax.set_xlim(0,10) # My
    ax.set_xticks([0,5,10])
    ax.set_xlabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_source_max':
    ax.set_xlim(0,10) # -
    ax.set_xlabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_source_host_max':
    ax.set_xlim(0,10) # -
    ax.set_xlabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM3_max':
    ax.set_xlim(0,5.0) # -
    ax.set_xlabel("Max. nr of OFM3 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM2_max':
    ax.set_xlim(0,5) # -
    ax.set_xlabel("Max. nr of OFM2 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OMF1_max':
    ax.set_xlim(0,5) # -
    ax.set_xlabel("Max. nr of OFM1 [-]",weight="bold",fontsize=ftsize)
  elif ax.get_xlabel() == 'n_OFM12_max':
    ax.set_xlim(0,OFM12_max) # -
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
    ax.set_ylim(350,600) # km
    ax.set_yticks([400,450,500,550])
    ax.set_yticklabels(craton_distance_labels)
    ax.set_ylabel("Initial craton-rift distance [km]",weight="bold",fontsize=ftsize)
  if ax.get_ylabel() == 'initial_fault_geometry':
    ax.set_ylabel("Initial fault geometry [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_migration':
    ax.set_ylim(0,10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start rift migration [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'migration_direction':
    ax.margins(x=0.2)
    ax.set_ylabel("Direction rift migration [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_left_border_fault':
    ax.set_ylim(0,10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start left border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_right_border_fault':
    ax.set_ylim(0,10) # My
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start right border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'start_border_fault':
    ax.set_ylim(0,25) # My
    ax.set_yticks([0,10,20,25])
    ax.set_ylabel("Start border fault(s) [My]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_source_max':
    ax.set_ylim(-0.,10.) # -
    ax.set_ylabel("Max. nr of source basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_source_host_max':
    ax.set_ylim(-0.,10.) # -
    ax.set_ylabel("Max. nr of source+host basins [-]",weight="bold",fontsize=ftsize)
  elif ax.get_ylabel() == 'n_OFM3_max':
    ax.set_ylim(-1.0,5.0) # -
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
