# Locate and count the number of dark green blobs
# in pngs that represent source and host rock.

import cv2
import numpy as np
import itertools
import pandas as pd
from os.path import exists
import time
print ("Numpy version: ", np.__version__)

###### Interactive? ######
interactive_summary = True
###### Factor to multiple vtu timestep number with to get the model time in My ######
vtu_step_to_time_in_My = 0.5

###### Store timestamp for reading and writing to file
timestr = '20241129-164950'

###### Path to models ######
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

###### Model names ######
models = [
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##@'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
]

####### Timesteps to look at images ######
ASPECT_time_steps = ['00000','00001','00002','00003','00004','00005','00006','00007','00008','00009','00010','00011','00012','00013','00014','00015','00016','00017','00018','00019','00020','00021','00022','00023','00024','00025','00026','00027','00028','00029','00030','00031','00032','00033','00034','00035','00036','00037','00038','00039','00040','00041','00042','00043','00044','00045','00046','00047','00048','00049','00050']

###### Create file paths ######
paths = [base+m for m in models]

###### Loop over requested models ######
for m in models:

  ###### Create dataframes to store output data ######
  # 2. frame for data summarizing the results of all timesteps
  dataframe_summary = pd.DataFrame(columns=['initial_fault_geometry','start_left_border_fault','start_right_border_fault','end_left_border_fault','end_right_border_fault','start_migration','end_migration','migration_direction','start_oceanic_spreading','n_source_max','n_source_host_max','n_OFM3_max','n_OFM1_max','n_OFM2_max'])

  ###### Read timestep output file ######
  dataframe = pd.read_csv(m+'/'+m+'_stats_'+timestr+'.csv')

  ###### Open each timestep ######
  if interactive_summary:
    for t in ASPECT_time_steps:
      img_all = cv2.imread(m+'/'+m+'_'+t+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_280000_25000.png')
      cv2.imshow("Original: All data at " + t, img_all)
      overlap_source_host_fault_contours_image = cv2.imread(m+'/'+m+'_'+t+'_bitwise_overlap_fault.png')
      cv2.imshow("Binary + Contours: Source and host rock overlaps active fault" + t, overlap_source_host_fault_contours_image)
      cv2.moveWindow("Binary + Contours: Source and host rock overlaps active fault" + t, 0, 250)
      cv2.waitKey(0)

  ###### Fill the summary table ######
  start_border_fault = np.nan
  end_border_fault = np.nan
  start_migration = np.nan
  end_migration = np.nan
  initial_geometry = 'X'
  migration_direction = 'X'
  start_spreading = np.nan
  if interactive_summary: 
    while True:
      try:  
        start_left_border_fault = float(input("Start left main border fault (vtu step): "))*vtu_step_to_time_in_My
        start_right_border_fault = float(input("Start right main border fault (vtu step): "))*vtu_step_to_time_in_My
        end_left_border_fault = float(input("End left main border fault (vtu step): "))*vtu_step_to_time_in_My
        end_right_border_fault = float(input("End right main border fault (vtu step): "))*vtu_step_to_time_in_My
        start_migration = float(input("Start migration (vtu step): "))*vtu_step_to_time_in_My
        end_migration = float(input("End migration (vtu step): "))*vtu_step_to_time_in_My
        initial_geometry = input("Initial fault geometry (C|C-RD|C-LD|Lside-Rdip|Rside-Ldip|Lside-Rdip Rside-ULCshear|Rside-Ldip Lside-ULCshear|Lside-ULCshear Lside-Rdip): ")
        migration_direction = input("Migration direction (L|C|R): ")
        start_spreading = float(input("Start oceanic spreading (vtu step): "))*vtu_step_to_time_in_My
        break
      except ValueError:
        print("Please enter valid value")
  dataframe_summary.loc[0,'start_left_border_fault'] = start_left_border_fault
  dataframe_summary.loc[0,'start_right_border_fault'] = start_right_border_fault
  dataframe_summary.loc[0,'end_left_border_fault'] = end_left_border_fault
  dataframe_summary.loc[0,'end_right_border_fault'] = end_right_border_fault
  dataframe_summary.loc[0,'start_migration'] = start_migration
  dataframe_summary.loc[0,'end_migration'] = end_migration
  dataframe_summary.loc[0,'initial_fault_geometry'] = initial_geometry
  dataframe_summary.loc[0,'migration_direction'] = migration_direction
  dataframe_summary.loc[0,'start_oceanic_spreading'] = start_spreading
  max_values = dataframe.max()
  dataframe_summary.loc[0,'n_source_max'] = max_values['n_source']
  dataframe_summary.loc[0,'n_source_host_max'] = max_values['n_source_host']
  dataframe_summary.loc[0,'n_OFM3_max'] = max_values['n_OFM3']
  dataframe_summary.loc[0,'n_OFM1_max'] = max_values['n_OFM1']
  dataframe_summary.loc[0,'n_OFM2_max'] = max_values['n_OFM2']

  ###### Write summary output file with same timestamp ######
  dataframe_summary.to_csv(m+'/'+m+'_stats_summary_'+timestr+'.csv',index=False,na_rep='nan')

  ###### Close all opened windows ######
  cv2.destroyAllWindows()