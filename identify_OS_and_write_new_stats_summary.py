# Locate and count the number of dark green blobs
# in pngs that represent source and host rock.

from tracemalloc import start
import cv2
import numpy as np
import itertools
import pandas as pd
from os.path import exists
import time
print ("Numpy version: ", np.__version__)

###### Interactive? ######
interactive_summary = True
###### Only cut the data with the start time of oceanic spreading? ######
cut_on_OS_only = False
###### Factor to multiple vtu timestep number with to get the model time in My ######
vtu_step_to_time_in_My = 0.5

###### Store timestamp for reading and writing to file
timestr = '20241128-171900'

###### Path to models ######
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

###### Model names ######
models = [
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@!'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
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
# CERI runs
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5o_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
#
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
##@!'5p_fixed_CERI_craton2000km_SWI2_minvisc5e18_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200',
]

####### Timesteps to look at images and sample data ######
ASPECT_time_steps = ['00035','00036','00037','00038','00039','00040','00041','00042','00043','00044','00045','00046','00047','00048','00049','00050']

###### Create file paths ######
paths = [base+m for m in models]

###### Loop over requested models ######
for m in models:

  ###### Create dataframes to store output data ######
  # 2. frame for data summarizing the results of all timesteps
  dataframe_summary_new = pd.DataFrame(columns=['initial_fault_geometry','start_left_border_fault','start_right_border_fault','end_left_border_fault','end_right_border_fault','start_migration','end_migration','migration_direction','start_oceanic_spreading','n_source_max','n_source_host_max','n_OFM3_max','n_OFM1_max','n_OFM2_max','n_OFM12_max'])

  ###### Read timestep output file ######
  dataframe = pd.read_csv(m+'/'+m+'_stats_'+timestr+'.csv', converters={'time': str,'migration_direction': str,'initial_fault_geometry': str})
  dataframe_summary = pd.read_csv(m+'/'+m+'_stats_summary_'+timestr+'.csv', converters={'time': str,'migration_direction': str,'initial_fault_geometry': str})

  ###### Open each timestep ######
  if interactive_summary:
    for t in ASPECT_time_steps:
      img_materials = cv2.imread(m+'/'+m+'_'+t+'_only_materials_zoom2_280000_25000.png')
      cv2.imshow("Original: All materials at " + t, img_materials)
      overlap_source_host_fault_contours_image = cv2.imread(m+'/'+m+'_'+t+'_bitwise_overlap_fault.png')
      cv2.imshow("Binary + Contours: Source and host rock overlaps active fault" + t, overlap_source_host_fault_contours_image)
      cv2.moveWindow("Binary + Contours: Source and host rock overlaps active fault" + t, 0, 250)
      cv2.waitKey(0)

  ###### Get time start spreading from user ######
  if interactive_summary and not cut_on_OS_only: 
    while True:
      try:  
        start_spreading_step = input("Start oceanic spreading (vtu step): ")
        start_spreading = float(start_spreading_step)*vtu_step_to_time_in_My
        break
      except ValueError:
        print("Please enter valid value")
  if cut_on_OS_only:
    start_spreading_step = dataframe_summary.loc[0,'start_oceanic_spreading']/vtu_step_to_time_in_My
    start_spreading = dataframe_summary.loc[0,'start_oceanic_spreading']

  ###### Fill the summary table based on old data + the new OS timestep ######
  dataframe_summary_new.loc[0,'start_left_border_fault'] = dataframe_summary.loc[0,'start_left_border_fault']
  dataframe_summary_new.loc[0,'start_right_border_fault'] = dataframe_summary.loc[0,'start_right_border_fault']
  dataframe_summary_new.loc[0,'end_left_border_fault'] = dataframe_summary.loc[0,'end_left_border_fault']
  dataframe_summary_new.loc[0,'end_right_border_fault'] = dataframe_summary.loc[0,'end_right_border_fault']
  dataframe_summary_new.loc[0,'start_migration'] = dataframe_summary.loc[0,'start_migration']
  dataframe_summary_new.loc[0,'end_migration'] = dataframe_summary.loc[0,'end_migration']
  dataframe_summary_new.loc[0,'initial_fault_geometry'] = dataframe_summary.loc[0,'initial_fault_geometry']
  dataframe_summary_new.loc[0,'migration_direction'] = dataframe_summary.loc[0,'migration_direction']
  dataframe_summary_new.loc[0,'start_oceanic_spreading'] = start_spreading
  dataframe_summary_new.loc[0,'n_source_max'] = dataframe_summary.loc[0,'n_source_max']
  dataframe_summary_new.loc[0,'n_source_host_max'] = dataframe_summary.loc[0,'n_source_host_max']
  dataframe_summary_new.loc[0,'n_OFM3_max'] = dataframe_summary.loc[0,'n_OFM3_max']
  dataframe_summary_new.loc[0,'n_OFM1_max'] = dataframe_summary.loc[0,'n_OFM1_max']
  dataframe_summary_new.loc[0,'n_OFM2_max'] = dataframe_summary.loc[0,'n_OFM2_max']
  dataframe_summary_new.loc[0,'n_OFM12_max'] = dataframe_summary.loc[0,'n_OFM12_max']

  ###### If OS occurs within the model run, cut all time measurements by that timestep of OS ######
  print ("Old vs new start OS: ",  dataframe_summary.loc[0,'start_oceanic_spreading'], start_spreading)
  if start_spreading < dataframe_summary.loc[0,'end_migration']:
    print ("Oceanic spreading starts before the end of rift migration.")
  if start_spreading <= 25.0:
    if 'n_OFM12' not in dataframe.columns:
      # sum OFM1 and OFM2
      dataframe['n_OFM12'] = dataframe[['n_OFM1','n_OFM2']].sum(axis=1)
    dataframe_cut = dataframe[dataframe["time"].le('000'+start_spreading_step)]
    max_values_cut = dataframe_cut.max()
    dataframe_summary_new.loc[0,'n_source_max'] = max_values_cut['n_source']
    dataframe_summary_new.loc[0,'n_source_host_max'] = max_values_cut['n_source_host']
    dataframe_summary_new.loc[0,'n_OFM3_max'] = max_values_cut['n_OFM3']
    dataframe_summary_new.loc[0,'n_OFM1_max'] = max_values_cut['n_OFM1']
    dataframe_summary_new.loc[0,'n_OFM2_max'] = max_values_cut['n_OFM2']
    dataframe_summary_new.loc[0,'n_OFM12_max'] = max_values_cut['n_OFM12']

  ###### Write summary output file with same timestamp ######
  if cut_on_OS_only:
    dataframe_summary_new.to_csv(m+'/'+m+'_stats_summary_cuttoOS_'+timestr+'.csv',index=False,na_rep='nan')
  else:
    dataframe_summary_new.to_csv(m+'/'+m+'_stats_summary_cuttonewOS_'+timestr+'.csv',index=False,na_rep='nan')

  ###### Close all opened windows ######
  cv2.destroyAllWindows()