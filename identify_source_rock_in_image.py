# Locate and count the number of dark green blobs
# in pngs that represent source and host rock.

import cv2
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Polygon
from shapely.geometry import LineString
from shapely.geometry import Point
from shapely.ops import unary_union
import shapely
import itertools
import pandas as pd
from os.path import exists
import time
print ("Shapely version: ", shapely.__version__)
print ("Numpy version: ", np.__version__)

###### Interactive? ######
interactive_OFM12 = True
interactive_OFM3 = True
interactive_summary = True
###### What buffer size [pixel] to use for intersections ######
buffer = 0
###### Factor to multiple vtu timestep number with to get the model time in My ######
vtu_step_to_time_in_My = 0.5

###### Store timestamp for writing to file
timestr = time.strftime("%Y%m%d-%H%M%S")

###### Path to models ######
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

###### Model names ######
models = [
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
]


###### Create file paths ######
paths = [base+m for m in models]
#ASPECT_time_steps = ['00000','00001','00005','00010','00015','00020','00025','00030','00035','00040','00045','00050']
#ASPECT_time_steps = ['00040','00041']
ASPECT_time_steps = ['00000','00001','00002','00003','00004','00005','00006','00007','00008','00009','00010','00011','00012','00013','00014','00015','00016','00017','00018','00019','00020','00021','00022','00023','00024','00025','00026','00027','00028','00029','00030','00031','00032','00033','00034','00035','00036','00037','00038','00039','00040','00041','00042','00043','00044','00045','00046','00047','00048','00049','00050']

###### Loop over requested models ######
for m in models:

  ###### Create dataframes to store output data ######
  # 1. frame for data for every timestep
  dataframe = pd.DataFrame(columns=['time','buffer','n_source_fault_overlaps','n_host_fault_overlaps','n_source_inactive_fault_overlaps','n_host_inactive_fault_overlaps','n_source','n_source_host','n_potential_OFM12','n_potential_OFM3','n_OFM3','n_OFM1','n_OFM2'])
  # 2. frame for data summarizing the results of all timesteps
  dataframe_summary = pd.DataFrame(columns=['initial_fault_geometry','start_border_fault', 'end_border_fault','start_migration','end_migration','migration_direction','start_oceanic_spreading','n_source_max','n_source_host_max','n_OFM3_max','n_OFM1_max','n_OFM2_max'])

  ###### Loop over requested timesteps ######
  index_model_time = 0
  for t in ASPECT_time_steps:

    ###### Store timestep and used buffer around polygons ######
    dataframe.loc[index_model_time, 'time'] = t
    dataframe.loc[index_model_time, 'buffer'] = buffer
    print ("Model name and timstep: ", m, t)

    ###### Read the input images ######
    img = cv2.imread(m+'/'+m+'_'+t+'_source_host_strain_strainrate_8_zoom2_280000_25000.png')
    img_all = cv2.imread(m+'/'+m+'_'+t+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_280000_25000.png')
    img_source = cv2.imread(m+'/'+m+'_'+t+'_source_8_zoom2_280000_25000.png')  
    img_host = cv2.imread(m+'/'+m+'_'+t+'_host_8_zoom2_280000_25000.png')  
    img_strainrate = cv2.imread(m+'/'+m+'_'+t+'_strainrate_8_zoom2_280000_25000.png')  
    img_strain = cv2.imread(m+'/'+m+'_'+t+'_plasticstrain_8_zoom2_280000_25000.png')  
    
    ###### Make sure the images exist ######
    assert img is not None, "File could not be read, check with os.path.exists()"
    assert img_all is not None, "File could not be read, check with os.path.exists()"
    assert img_source is not None, "File could not be read, check with os.path.exists()"
    assert img_host is not None, "File could not be read, check with os.path.exists()"
    assert img_strainrate is not None, "File could not be read, check with os.path.exists()"
    assert img_strain is not None, "File could not be read, check with os.path.exists()"
    
    ###### Mask OFM ingredients ######
    # 1. Source rock
    img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 254, 255, cv2.THRESH_BINARY)
    source_rock = cv2.bitwise_not(thresh)
    cv2.imwrite(m+'/'+m+'_'+t+'_gray_threshold_inverted_source.png', source_rock)

    # 2. Host rock
    img_gray = cv2.cvtColor(img_host, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 254, 255, cv2.THRESH_BINARY)
    host_rock = cv2.bitwise_not(thresh)
    cv2.imwrite(m+'/'+m+'_'+t+'_gray_threshold_inverted_host.png', host_rock)
    
    # 3. Strain rate
    img_gray = cv2.cvtColor(img_strainrate, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY)
    active_fault_zone = cv2.bitwise_not(thresh)
    cv2.imwrite(m+'/'+m+'_'+t+'_gray_threshold_inverted_fault.png', active_fault_zone) 
    
    # 4. Plastic strain
    img_gray = cv2.cvtColor(img_strain, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY)
    inactive_fault_zone = cv2.bitwise_not(thresh)
    cv2.imwrite(m+'/'+m+'_'+t+'_gray_threshold_inverted_inactive_fault.png', inactive_fault_zone) 

    ###### Get contours of individual OFM elements ######
    # Get the contours of source rock area
    source_rock_contours, source_rock_hierarchy = cv2.findContours(source_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Contours: Nr source rock areas = " + str(len(source_rock_contours)))
    
    # Get the contours of host rock area
    host_rock_contours, host_rock_hierarchy = cv2.findContours(host_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Contours: Nr host rock areas = " + str(len(host_rock_contours)))
    
    # Get the contours of active fault zone area
    fault_contours, fault_hierarchy = cv2.findContours(active_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Contours: Nr active faults = " + str(len(fault_contours)))
    
    # Get the contours of inactive fault zone area
    inactive_fault_contours, inactive_fault_hierarchy = cv2.findContours(inactive_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Contours: Nr inactive faults = " + str(len(inactive_fault_contours)) + "\n")

    # Get rid of any contours that are too small
    def remove_small_contours(min_contour_size, contours):
      tmp_contours = []
      for c in contours:
        if cv2.contourArea(c) > min_contour_size:
          tmp_contours.append(c)
      return tuple(tmp_contours)

    # The minimum nr of pixels a contour should encompass
    min_contour_size = 1

    source_rock_contours = remove_small_contours(min_contour_size, source_rock_contours)
    contour_source_image = cv2.cvtColor(source_rock.copy(), cv2.COLOR_GRAY2RGB)
    cv2.drawContours(contour_source_image, source_rock_contours, -1, (0,0,255), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_source_area.png', contour_source_image)
    print("Contours: Nr large source rock areas = " + str(len(source_rock_contours)))

    contour_host_image = cv2.cvtColor(host_rock.copy(), cv2.COLOR_GRAY2RGB)
    host_rock_contours = remove_small_contours(min_contour_size, host_rock_contours)
    cv2.drawContours(contour_host_image, host_rock_contours, -1, (0,0,255), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_host_area.png', contour_host_image)
    print("Contours: Nr large host rock areas = " + str(len(host_rock_contours)))

    contour_fault_image = cv2.cvtColor(active_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    fault_contours = remove_small_contours(min_contour_size, fault_contours)
    cv2.drawContours(contour_fault_image, fault_contours, -1, (0,0,255), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_fault_area.png', contour_fault_image)
    print("Contours: Nr large active fault areas = " + str(len(fault_contours)))
    
    contour_inactive_fault_image = cv2.cvtColor(inactive_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    inactive_fault_contours = remove_small_contours(min_contour_size, inactive_fault_contours)
    cv2.drawContours(contour_inactive_fault_image, inactive_fault_contours, -1, (0,0,255), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_inactive_fault_area.png', contour_inactive_fault_image)
    print("Contours: Nr large inactive fault areas = " + str(len(inactive_fault_contours)) + "\n")

    ###### Finding intersections with 2 methods ######
    # 1. Using binary logic: find overlaps but no OFMs
   
    ###### Check for overlaps bitwise ######
    overlap_source_fault = cv2.bitwise_and(source_rock, active_fault_zone)
    overlap_host_fault = cv2.bitwise_and(host_rock, active_fault_zone)
    overlap_source_inactive_fault = cv2.bitwise_and(source_rock, inactive_fault_zone)
    overlap_host_inactive_fault = cv2.bitwise_and(host_rock, inactive_fault_zone)
    # Potential OFM12
    overlap_source_host_fault = cv2.bitwise_or(overlap_source_fault, overlap_host_fault)
    # Potential OFM3
    overlap_source_host_inactive_fault = cv2.bitwise_or(overlap_source_inactive_fault, overlap_host_inactive_fault)
    # To check whether OFM12 or OFM3 occurs when both strain rate and strain are present
    overlap_source_active_inactive_fault = cv2.bitwise_and(overlap_source_fault, overlap_source_inactive_fault)
    
    ###### Get contours of bitwise overlaps and report ######
    # Function to create a random BGR color
    def create_random_color():
      color = np.random.randint(0, 255, size=(3, ))
      #convert data types int64 to int
      color = ( int (color [ 0 ]), int (color [ 1 ]), int (color [ 2 ]))
      return tuple(color)

    # Source rock intersection with active fault
    overlap_source_fault_contours, overlap_source_fault_hierarchy = cv2.findContours(overlap_source_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_fault_contours = remove_small_contours(min_contour_size, overlap_source_fault_contours)
    print("Binary + Contours: Nr source rock overlaps active fault = " + str(len(overlap_source_fault_contours)))
    dataframe.loc[index_model_time, 'n_source_fault_overlaps'] = len(overlap_source_fault_contours)
    overlap_source_fault_image = cv2.cvtColor(active_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    # Draw each contour with own color
    for c in overlap_source_fault_contours:
      cv2.drawContours(overlap_source_fault_image, c, -1, create_random_color(), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_source_fault.png', overlap_source_fault_image)
    
    # Source rock intersection with inactive fault
    overlap_source_inactive_fault_contours, overlap_source_inactive_fault_hierarchy = cv2.findContours(overlap_source_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_inactive_fault_contours = remove_small_contours(min_contour_size, overlap_source_inactive_fault_contours)
    print("Binary + Contours: Nr source rock overlaps inactive fault = " + str(len(overlap_source_inactive_fault_contours)))
    dataframe.loc[index_model_time, 'n_source_inactive_fault_overlaps'] = len(overlap_source_inactive_fault_contours)
    overlap_source_inactive_fault_image = cv2.cvtColor(inactive_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    # Draw each contour with own color
    for c in overlap_source_inactive_fault_contours:
      cv2.drawContours(overlap_source_inactive_fault_image, c, -1, create_random_color(), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_source_inactive_fault.png', overlap_source_inactive_fault_image)
    
    # Host rock intersection with active fault
    overlap_host_fault_contours, overlap_host_fault_hierarchy = cv2.findContours(overlap_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_host_fault_contours = remove_small_contours(min_contour_size, overlap_host_fault_contours)
    print("Binary + Contours: Nr host rock overlaps active fault = " + str(len(overlap_host_fault_contours)))
    dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = len(overlap_host_fault_contours)
    overlap_host_fault_image = cv2.cvtColor(active_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    # Draw each contour with own color
    for c in overlap_host_fault_contours:
      cv2.drawContours(overlap_host_fault_image, c, -1, create_random_color(), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_host_fault.png', overlap_host_fault_image)
    
    # Host rock intersection with inactive fault
    overlap_host_inactive_fault_contours, overlap_host_inactive_fault_hierarchy = cv2.findContours(overlap_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_host_inactive_fault_contours = remove_small_contours(min_contour_size, overlap_host_inactive_fault_contours)
    print("Binary + Contours: Nr host rock overlaps inactive fault = " + str(len(overlap_host_inactive_fault_contours)) + "\n")
    dataframe.loc[index_model_time, 'n_host_inactive_fault_overlaps'] = len(overlap_host_inactive_fault_contours)
    overlap_host_inactive_fault_image = cv2.cvtColor(inactive_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    # Draw each contour with own color
    for c in overlap_host_inactive_fault_contours:
      cv2.drawContours(overlap_host_inactive_fault_image, c, -1, create_random_color(), 1)
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_host_inactive_fault.png', overlap_host_inactive_fault_image)

    # Source and host rock intersection with active fault
    overlap_source_host_fault_contours, overlap_source_host_fault_hierarchy = cv2.findContours(overlap_source_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_host_fault_contours = remove_small_contours(min_contour_size, overlap_source_host_fault_contours)
    print("Binary + Contours: Nr source and host rock overlaps active fault = " + str(len(overlap_source_host_fault_contours)))

    # Source rock intersection with active and inactive fault
    overlap_source_active_inactive_fault_contours, overlap_source_active_inactive_fault_hierarchy = cv2.findContours(overlap_source_active_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_active_inactive_fault_contours = remove_small_contours(min_contour_size, overlap_source_active_inactive_fault_contours)
    print("Binary + Contours: Nr source rock overlaps active and inactive fault = " + str(len(overlap_source_active_inactive_fault_contours)))

    # Source and host rock intersection with inactive fault
    overlap_source_host_inactive_fault_contours, overlap_source_host_inactive_fault_hierarchy = cv2.findContours(overlap_source_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_host_inactive_fault_contours = remove_small_contours(min_contour_size, overlap_source_host_inactive_fault_contours)
    print("Binary + Contours: Nr source and host rock overlaps inactive fault = " + str(len(overlap_source_host_inactive_fault_contours)) + "\n")
    
    ###### Plot the source and host rock contours on top of faults ######
    # active fault
    overlap_source_host_fault_contours_image = img_strainrate.copy()
    cv2.drawContours(overlap_source_host_fault_contours_image, source_rock_contours, -1, (0,0,255), 1) # red
    cv2.drawContours(overlap_source_host_fault_contours_image, host_rock_contours, -1, (255,0,0), 1) # blue
    # inactive fault
    overlap_source_host_inactive_fault_contours_image = img_strain.copy()
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, source_rock_contours, -1, (0,0,255), 1) # red
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, host_rock_contours, -1, (255,0,0), 1) # blue
    
    ###### Plot binary overlaps on top of source and host rock contours and faults - !these should be used for OFM analysis! ######
    # active fault
    cv2.drawContours(overlap_source_host_fault_contours_image, overlap_source_host_fault_contours, -1, (0,255,0), 3) # green
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_fault.png', overlap_source_host_fault_contours_image)
    # inactive fault
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, overlap_source_host_inactive_fault_contours, -1, (0,255,0), 3) # green
    # source and host that are already linked to active fault
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, overlap_source_host_fault_contours, -1, (0,0,0), 2) # black
    cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_inactive_fault.png', overlap_source_host_inactive_fault_contours_image)

    ###### ######
    # 2. Using polygons from Shapely: find OFMs
    # variables containing overlaps found with Shapely end in 'overlaps',
    # while those found with the binary logic and contours begin with 'overlap'.

    ###### Loop over active faults and check for overlap with source and host rock with Shapely ######
    # Counters for the overlaps
    n_source_fault_overlaps = 0
    n_host_fault_overlaps = 0
    # Per fault, count the overlaps
    source_fault_overlaps = np.zeros(len(fault_contours))
    host_fault_overlaps = np.zeros(len(fault_contours))
    # Per fault, indicate the contour of the source or host that overlaps
    i_source_fault_overlaps = np.zeros(len(fault_contours))
    i_host_fault_overlaps = np.zeros(len(fault_contours))
    # Fault index
    p = 0

    # Plot the OFMs on top of strain rate and source and host contours
    img_OFM12_contours = img_strainrate.copy()
    cv2.drawContours(img_OFM12_contours, source_rock_contours, -1, (0,0,255), 1) # red
    cv2.drawContours(img_OFM12_contours, host_rock_contours, -1, (255,0,0), 1) # blue

    # Loop over each fault contour
    for contour in fault_contours:
      intersect_source = False
      intersect_host = False
      fault_polygon = Polygon()

      # Create fault polygon and pad it with user-set buffer
      if len(contour) > 2:
        fault_polygon = Polygon([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 2:
        fault_polygon = LineString([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 1:
        fault_polygon = Point(contour[0][0]).buffer(buffer)
        print("Fault polygon is point")
      else:
        print ("Fault contour empty")

      # Loop over all source rock contours
      s = 0
      for source_contour in source_rock_contours:
        source_polygon = Polygon()
        # Create source polygon and pad it with user-set buffer
        if len(source_contour) > 2:
          source_polygon = Polygon([l[0] for l in source_contour]).buffer(buffer)
        # Create a line instead of a polygon
        elif len(source_contour) == 2:
          source_polygon = LineString([l[0] for l in source_contour]).buffer(buffer)
        # Create a point instead of a polygon
        elif len(source_contour) == 1:
          source_polygon = Point(contour[0][0]).buffer(buffer)
          print("Source polygon is point")
        else:
          print ("Source rock contour empty")

        # Check for overlap fault and source rock
        if (fault_polygon.intersects(source_polygon) or fault_polygon.touches(source_polygon) or source_polygon.within(fault_polygon) or fault_polygon.within(source_polygon) or source_polygon.overlaps(fault_polygon) or fault_polygon.covers(source_polygon) or fault_polygon.crosses(source_polygon) ):
          intersect_source = True
        if (len(source_contour) == 1 and source_polygon.within(fault_polygon)):
          intersect_source = True
        # Draw and count if overlap occurs
        if intersect_source:
          cv2.drawContours(img_OFM12_contours, source_contour,-1,(0,255,0),3) # green
          n_source_fault_overlaps += 1
          source_fault_overlaps[p] += 1
          i_source_fault_overlaps[p] = s
        # Reset for next source
        intersect_source = False
        s += 1

      # Loop over host contours
      h = 0
      for host_contour in host_rock_contours:
        host_polygon = Polygon()
        # Create host polygon and pad it with user-set buffer
        if len(host_contour) > 2:
          host_polygon = Polygon([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 2:
          host_polygon = LineString([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 1:
          host_polygon = Point(host_contour[0][0]).buffer(buffer)
          print("Host polygon is point")
        else:
          print ("Host rock contour empty")

        # Check for overlap fault and host rock
        if (fault_polygon.intersects(host_polygon) or fault_polygon.touches(host_polygon) or host_polygon.within(fault_polygon) or fault_polygon.within(host_polygon) or host_polygon.overlaps(fault_polygon) or fault_polygon.covers(host_polygon) or fault_polygon.crosses(host_polygon) ):
          intersect_host = True
        if (len(host_contour) == 1 and host_polygon.within(fault_polygon)):
          intersect_host = True
        if intersect_host:
          cv2.drawContours(img_OFM12_contours, host_contour,-1,(0,255,0),3) # green
          n_host_fault_overlaps += 1
          host_fault_overlaps[p] += 1
          i_host_fault_overlaps[p] = h
          # If both source and host overlap with this fault,
          # plot their contour in different colour
          # NB several host contours might overlap for one source
          # contour, so this source contour will be plotted multiple
          # times
          #if source_fault_overlaps[p] > 0:
          #  if len(source_rock_contours[int(i_source_fault_overlaps[p])]) > 0:
          #    cv2.drawContours(img_OFM12_contours, source_rock_contours[int(i_source_fault_overlaps[p])],-1,(0,255,255),3) 
          #  cv2.drawContours(img_OFM12_contours, host_contour,-1,(240,32,160),3)
        #else:
        #  cv2.drawContours(img_OFM12_contours, host_contour,-1,(0,0,255),1)
        # Reset for next host
        intersect_host = False
        h += 1

      # Update fault contour counter
      p += 1

    # Save and print output
    print("Shapely: Nr source rock overlaps active fault with buffer of", buffer, " = ", n_source_fault_overlaps)
    #dataframe.loc[index_model_time, 'n_source_fault_overlaps'] = n_source_fault_overlaps
    print("Shapely: Nr host rock overlaps active fault with buffer of", buffer, " = ", n_host_fault_overlaps)
    #dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = n_host_fault_overlaps

    # Check which fault overlaps with both source and host rock, print and save
    # Note that they are only potential OFM12s, because a fault can be connected at
    # depth to another fault and they will be counted as one.
    source_host_fault_overlaps = (source_fault_overlaps != 0) & (host_fault_overlaps != 0)
    print ("Shapely: Nr of potential OFM12s: ", np.count_nonzero(source_host_fault_overlaps), "\n")
    dataframe.loc[index_model_time, 'n_potential_OFM12'] = np.count_nonzero(source_host_fault_overlaps)
    
    ###### Save the OFM12 source and host on top of strainrate - this figure should be used for OFMs ######
    cv2.imwrite(m+'/'+m+'_'+t+'_Shapely_buffer_'+str(buffer)+'_OFM12.png', img_OFM12_contours)
    
    ###### Open the OFM12 image and ask user for n_OFM1 and n_OFM2 ######
    n_source = np.nan
    n_source_host = np.nan
    n_OFM1 = np.nan
    n_OFM2 = np.nan
    if len(source_rock_contours) > 0:
      # Ask user for interpretation
      if interactive_OFM12 and ((len(overlap_source_host_fault_contours) > 0) or (np.count_nonzero(source_host_fault_overlaps) > 0)):
        cv2.imshow("Shapely: Possible OFM1 and OFM2", img_OFM12_contours)
        cv2.imshow("Binary: Source, host, strainrate contours", overlap_source_host_fault_contours_image)
        cv2.moveWindow("Binary: Source, host, strainrate contours", 0, 250)
        cv2.imshow("Original: All data", img_all)
        cv2.moveWindow("Original: All data", 0, 500)
        cv2.waitKey(0)
        while True:
          try:
            n_source = int(input(F'Nr of basins with source (potentially {len(source_rock_contours)}): '))
            n_source_host = input("Nr of basins with source and host: ")
            n_OFM1 = int(input(F'Nr of OFM1 (potentially {np.count_nonzero(source_host_fault_overlaps)}): '))
            n_OFM2 = int(input(F'Nr of OFM2 (potentially {np.count_nonzero(source_host_fault_overlaps)}): '))
            break
          except ValueError:
            print("Please enter valid integer")
        cv2.destroyAllWindows()
    else:
      n_source = 0
      n_source_host = 0
      n_OFM1 = 0
      n_OFM2 = 0

    # Save data
    dataframe.loc[index_model_time, 'n_source'] = n_source
    dataframe.loc[index_model_time, 'n_source_host'] = n_source_host
    dataframe.loc[index_model_time, 'n_OFM1'] = n_OFM1
    dataframe.loc[index_model_time, 'n_OFM2'] = n_OFM2

    # Print data 
    print("Shapely + visual inspection: Nr OFM1 with buffer of", buffer, " = ", n_OFM1)
    print("Shapely + visual inspection: Nr OFM2 with buffer of", buffer, " = ", n_OFM2, "\n")

    ###### Loop over inactive faults and check for each fault whether there is overlap with source and/or host rock ######
    n_source_inactive_fault_overlaps = 0
    n_host_inactive_fault_overlaps = 0
    # Per fault, count the overlaps
    source_inactive_fault_overlaps = np.zeros(len(inactive_fault_contours))
    host_inactive_fault_overlaps = np.zeros(len(inactive_fault_contours))
    # Per fault, indicate the contour of the source or host that overlaps
    i_source_inactive_fault_overlaps = np.zeros(len(inactive_fault_contours))
    i_host_inactive_fault_overlaps = np.zeros(len(inactive_fault_contours))
    # Fault index
    p = 0

    # Plot contours on top of strain
    img_OFM3_contours = img_strain.copy()
    cv2.drawContours(img_OFM3_contours, source_rock_contours, -1, (0,0,255), 3) # red
    cv2.drawContours(img_OFM3_contours, host_rock_contours, -1, (255,0,0), 3) # blue

    # Loop over inactive fault contours until all overlapping source and host rock is found
    for contour in inactive_fault_contours:
      intersect_source = False
      intersect_host = False
      fault_polygon = Polygon()

      # Create inactive fault polygon and pad it with user-set buffer
      if len(contour) > 2:
        fault_polygon = Polygon([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 2:
        fault_polygon = LineString([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 1:
        fault_polygon = Point(contour[0][0]).buffer(buffer)
        print("Fault polygon is point")
      else:
        print ("Fault contour empty")

      # Loop over source contours
      s = 0
      for source_contour in source_rock_contours:
        source_polygon = Polygon()
        # Create source polygon and pad it with user-set buffer
        if len(source_contour) > 2:
          source_polygon = Polygon([l[0] for l in source_contour]).buffer(buffer)
        elif len(source_contour) == 2:
          source_polygon = LineString([l[0] for l in source_contour]).buffer(buffer)
        elif len(source_contour) == 1:
          source_polygon = Point(source_contour[0][0]).buffer(buffer)
          print("Source polygon is point")
        else:
          print ("Source rock contour empty")

        # Check for overlap fault and source rock
        if (fault_polygon.intersects(source_polygon) or fault_polygon.touches(source_polygon) or source_polygon.within(fault_polygon) or fault_polygon.within(source_polygon) or source_polygon.overlaps(fault_polygon) or fault_polygon.covers(source_polygon) or fault_polygon.crosses(source_polygon) ):
          intersect_source = True
        if (len(source_contour) == 1 and source_polygon.within(fault_polygon)):
          intersect_source = True
        # Draw and count if overlap occurs
        if intersect_source:
          cv2.drawContours(img_OFM3_contours, source_contour,-1,(0,255,0),1) # green
          n_source_inactive_fault_overlaps += 1
          source_inactive_fault_overlaps[p] += 1
          i_source_inactive_fault_overlaps[p] = s
        # Reset for next source
        intersect_source = False
        s += 1

      h = 0
      for host_contour in host_rock_contours:
        intersect_host = False
        host_polygon = Polygon()
        # Create host polygon and pad it with user-set buffer
        if len(host_contour) > 2:
          host_polygon = Polygon([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 2:
          host_polygon = LineString([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 1:
          host_polygon = Point(host_contour[0][0]).buffer(buffer)
          print("Host polygon is point")
        else:
          print ("Host rock contour empty")

        # Check for overlap fault and host rock
        if (fault_polygon.intersects(host_polygon) or fault_polygon.touches(host_polygon) or host_polygon.within(fault_polygon) or fault_polygon.within(host_polygon) or host_polygon.overlaps(fault_polygon) or fault_polygon.covers(host_polygon) or fault_polygon.crosses(host_polygon) ):
           intersect_host = True
        if (len(host_contour) == 1 and host_polygon.within(fault_polygon)):
           intersect_host = True
        if intersect_host:
          cv2.drawContours(img_OFM3_contours, host_contour,-1,(0,255,0),1) # green
          n_host_inactive_fault_overlaps += 1
          host_inactive_fault_overlaps[p] += 1
          i_host_inactive_fault_overlaps[p] = h

        # Reset for next host
        intersect_host = False
        h += 1

        # TODO Create unions of source + host + inactive faults and count?
        #host_inactive_fault_union_polygon = unary_union([fault_polygon,host_polygon])

      # Update fault contour counter
      p += 1


    ###### Print and save data ######
    print("Shapely: Nr source rock overlaps inactive fault with buffer of", buffer, " = ", n_source_inactive_fault_overlaps)
    print("Shapely: Nr host rock overlaps inactive fault with buffer of", buffer, " = ", n_host_inactive_fault_overlaps)
    #dataframe.loc[index_model_time, 'n_source_inactive_fault_overlaps'] = n_source_inactive_fault_overlaps
    #dataframe.loc[index_model_time, 'n_host_inactive_fault_overlaps'] = n_host_inactive_fault_overlaps

    # Check which inactive fault overlaps with both source and host rock, print and save
    # Note that they are only potential OFM3s, because an inactive fault can be connected at
    # depth to another fault and they will be counted as one.
    source_host_inactive_fault_overlaps = (source_inactive_fault_overlaps != 0) & (host_inactive_fault_overlaps != 0)
    n_potential_OFM3 = np.count_nonzero(source_host_inactive_fault_overlaps)
    print ("Shapely: Nr of potential OFM3s with buffer of ", buffer, " = ", n_potential_OFM3, "\n")
    dataframe.loc[index_model_time, 'n_potential_OFM3'] = n_potential_OFM3

    ###### Save the OFM3 source and host on top of strain ######
    cv2.imwrite(m+'/'+m+'_'+t+'_Shapely_buffer_'+str(buffer)+'_OFM3.png', img_OFM3_contours)

    ###### If requested, check OFM3s interactively ######
    # But only if there is a chance of OFM3
    n_OFM3 = np.nan
    if interactive_OFM3 and len(source_rock_contours) > 0 and (n_potential_OFM3 > 0 or len(overlap_source_host_inactive_fault_contours) > 0):
      cv2.imshow("Shapely: Possible OFM3", img_OFM3_contours)
      cv2.imshow("Binary: Source, host, strain contours", overlap_source_host_inactive_fault_contours_image)
      cv2.moveWindow("Binary: Source, host, strain contours", 0, 250)
      cv2.imshow("Original: All data", img_all)
      cv2.moveWindow("Original: All data", 0, 500)
      cv2.waitKey(0)
      while True:
        try:
          n_OFM3 = int(input(F'Nr of OFM3 (potentially {n_potential_OFM3}): '))
          break
        except ValueError:
          print("Please enter valid integer")
      cv2.destroyAllWindows()
    elif len(source_rock_contours) == 0:
      n_OFM3 = 0

    print("Shapely + visual inspection: Nr OFM3 with buffer of", buffer, " = ", n_OFM3)
    dataframe.loc[index_model_time, 'n_OFM3'] = n_OFM3
    
    ###### Look at initial fault geometry and rift stabilization
    first_timesteps = ASPECT_time_steps[:20]
    last_timesteps = ASPECT_time_steps[-5:]
    if interactive_summary and (t in first_timesteps):
      cv2.imshow("Original: All data at " + t, img_all)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    if interactive_summary and (t in last_timesteps):
      cv2.imshow("Original: All data at " + t, img_all)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

    ###### Write output file with timestamp to avoid overwriting ######
    dataframe.to_csv(m+'/'+m+'_stats_'+timestr+'.csv',index=False,na_rep='nan')

    ###### Update output file index ######
    index_model_time += 1

  ###### Fill the summary table
  start_border_fault = np.nan
  end_border_fault = np.nan
  start_migration = np.nan
  end_migration = np.nan
  initial_geometry = 'X'
  migration_direction = 'X'
  start_spreading = np.nan
  if interactive_summary:
    while True:
      timestep = str(input("Timestep to look at again (eg 00005): "))
      if timestep in ASPECT_time_steps:
        print("Reviewing timestep " + timestep)
        cv2.imread(m+'/'+m+'_'+timestep+'_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_280000_25000.png')
        cv2.imshow("Original: All data at " + timestep, img_all)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
      else:
        break  
    while True:
      try:  
        start_border_fault = float(input("Start border fault (vtu step): "))*vtu_step_to_time_in_My
        end_border_fault = float(input("End border fault (vtu step): "))*vtu_step_to_time_in_My
        start_migration = float(input("Start migration (vtu step): "))*vtu_step_to_time_in_My
        end_migration = float(input("End migration (vtu step): "))*vtu_step_to_time_in_My
        initial_geometry = input("Initial fault geometry (C|C-RD|C-LD|Lside-Rdip|Rside-Ldip|Lside-Rdip Rside-ULCshear|Rside-Ldip Lside-ULCshear): ")
        migration_direction = input("Migration direction (L|C|R): ")
        start_spreading = float(input("Start oceanic spreading (vtu step): "))*vtu_step_to_time_in_My
        break
      except ValueError:
        print("Please enter valid value")
  dataframe_summary.loc[0,'start_border_fault'] = start_border_fault
  dataframe_summary.loc[0,'end_border_fault'] = end_border_fault
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