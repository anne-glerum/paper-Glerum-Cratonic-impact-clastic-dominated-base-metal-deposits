# Locate and count the number of dark green blobs
# in pngs that represent source rockn_source.

import cv2
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Polygon
from shapely.geometry import LineString
from shapely.geometry import Point
import shapely
import itertools
import pandas as pd
print (shapely.__version__)

###### Interactive? ######
interactive = False
###### What buffer size [pixel] to use for intersections ######
buffer = 1


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
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
]


###### Create file paths ######
paths = [base+m for m in models]
ASPECT_time_steps = ['00000','00001','00005','00010','00015','00020','00025','00030','00035','00040','00045','00050']
ASPECT_time_steps = ['00045']

###### Loop over requested models ######
for m in models:

  ###### Create dataframe to store output data ######
  dataframe = pd.DataFrame(columns=['time','buffer','n_host','n_source_fault_overlaps','n_host_fault_overlaps','n_source_inactive_fault_overlaps', 'n_host_inactive_fault_overlaps','n_source','n_source_host','n_OFM12','n_OFM3','n_OFM1','n_OFM2'])

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
    img_source_host = cv2.imread(m+'/'+m+'_'+t+'_source_host_8_zoom2_280000_25000.png')  
    img_strainrate = cv2.imread(m+'/'+m+'_'+t+'_strainrate_8_zoom2_280000_25000.png')  
    img_strain = cv2.imread(m+'/'+m+'_'+t+'_plasticstrain_8_zoom2_280000_25000.png')  
    
    ###### Make sure the images exist ######
    assert img is not None, "File could not be read, check with os.path.exists()"
    assert img_all is not None, "File could not be read, check with os.path.exists()"
    assert img_source_host is not None, "File could not be read, check with os.path.exists()"
    assert img_strainrate is not None, "File could not be read, check with os.path.exists()"
    assert img_strain is not None, "File could not be read, check with os.path.exists()"
    
    ###### Mask OFM ingredients ######
    # 1. Source rock
    # Build a mask where all dark green pixels are 255 and other colors are 0.
    # The two tuples provide the lower and upper bounds for dark green (0,85,0).
    source_rock = cv2.inRange(img_source_host, (0, 82, 0), (5, 88, 5))  
    
    # Build a mask where all light green pixels are 255 and other colors are 0.
    # 2. Host rock
    # Original RGBs:
    # Limestones 186 228 179
    # Carbonates 166 196 118
    # Silicates 35 139 69
    # The two tuples provide the lower and upper bounds in BGR!
    host_rock_1 = cv2.inRange(img, (165, 217, 179), (171, 223, 185))  
    host_rock_2 = cv2.inRange(img, (108, 187, 160), (114, 193, 166))  
    host_rock_3 = cv2.inRange(img, (62, 132, 31), (68, 138, 37))
    # Combine the three different host rocks into one.
    tmp_host_rock = cv2.bitwise_or(host_rock_1,host_rock_2)
    host_rock = cv2.bitwise_or(tmp_host_rock,host_rock_3)
    
    # Build a mask where all black pixels are 255 and other colors are 0.
    # 3. Strain rate
    # The two tuples provide the lower and upper bounds for greys.
    active_fault_zone = cv2.inRange(img_strainrate, (0, 0, 0), (250, 250, 250))  
    
    # Build a mask where all grey pixels are 255 and other colors are 0.
    # 4. Plastic strain
    # The two tuples provide the lower and upper bounds for greys.
    inactive_fault_zone = cv2.inRange(img_strain, (0, 0, 0), (230, 230, 230))
    
    ###### Finding intersection with 2 methods ######
    # 1. Using binary logic
   
    ###### Check for overlaps bitwise ######
    overlap_source_fault = cv2.bitwise_and(source_rock, active_fault_zone)
    overlap_host_fault = cv2.bitwise_and(host_rock, active_fault_zone)
    overlap_source_inactive_fault = cv2.bitwise_and(source_rock, inactive_fault_zone)
    overlap_host_inactive_fault = cv2.bitwise_and(host_rock, inactive_fault_zone)
    overlap_source_host_fault = cv2.bitwise_or(overlap_source_fault, overlap_host_fault)
    overlap_source_host_inactive_fault = cv2.bitwise_or(overlap_source_inactive_fault, overlap_host_inactive_fault)
    
    ###### Get contours of bitwise overlaps ######
    # Source rock intersection with active fault
    overlap_source_fault_contours, overlap_source_fault_hierarchy = cv2.findContours(overlap_source_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock overlaps with active fault found with binary logic = " + str(len(overlap_source_fault_contours)))
    #overlap_source_fault_image = cv2.cvtColor(overlap_source_fault.copy(), cv2.COLOR_GRAY2RGB)
    #cv2.drawContours(overlap_source_fault_image, overlap_source_fault_contours, -1, (0,0,255), 3)
    #cv2.imwrite(m+'/'+m+'_'+t+'_bitwise_overlap_source_fault.png', overlap_source_fault_image)
    
    # Source rock intersection with inactive fault
    overlap_source_inactive_fault_contours, overlap_source_inactive_fault_hierarchy = cv2.findContours(overlap_source_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock overlaps with inactive fault found with binary logic = " + str(len(overlap_source_inactive_fault_contours)))
    
    # Host rock intersection with active fault
    overlap_host_fault_contours, overlap_host_fault_hierarchy = cv2.findContours(overlap_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of host rock overlaps with active fault found with binary logic = " + str(len(overlap_host_fault_contours)))
    #dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = len(overlap_host_fault_contours)
    
    # Host rock intersection with inactive fault
    overlap_host_inactive_fault_contours, overlap_host_inactive_fault_hierarchy = cv2.findContours(overlap_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of host rock overlaps with inactive fault found with binary logic = " + str(len(overlap_host_inactive_fault_contours)))
    dataframe.loc[index_model_time, 'n_host_inactive_fault_overlaps'] = len(overlap_host_inactive_fault_contours)
    
    # Source and host rock intersection with active fault
    overlap_source_host_fault_contours, overlap_source_host_fault_hierarchy = cv2.findContours(overlap_source_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # Source and host rock intersection with inactive fault
    overlap_source_host_inactive_fault_contours, overlap_source_host_inactive_fault_hierarchy = cv2.findContours(overlap_source_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    ###### ######
    # 2. Using polygons from Shapely

    ###### Get contours of individual OFM elements ######
    # Get the contours of source rock area
    source_rock_contours, source_rock_hierarchy = cv2.findContours(source_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock contours found = " + str(len(source_rock_contours)))
    
    # Get the contours of host rock area
    host_rock_contours, host_rock_hierarchy = cv2.findContours(host_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    dataframe.loc[index_model_time, 'n_host'] = len(host_rock_contours)
    
    # Get the contours of active fault zone area
    fault_contours, fault_hierarchy = cv2.findContours(active_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    # Get the contours of inactive fault zone area
    inactive_fault_contours, inactive_fault_hierarchy = cv2.findContours(inactive_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    ###### Plot the source and host rock contours on top of faults ######
    overlap_source_host_fault_contours_image = img_strainrate.copy()
    overlap_source_host_inactive_fault_contours_image = img_strain.copy()
    cv2.drawContours(overlap_source_host_fault_contours_image, source_rock_contours, -1, (0,0,255), 3)
    cv2.drawContours(overlap_source_host_fault_contours_image, host_rock_contours, -1, (255,0,0), 3)
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, source_rock_contours, -1, (0,0,255), 3)
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, host_rock_contours, -1, (255,0,0), 3)
    
    ###### Plot overlaps on top of source and host rock contours and faults ######
    cv2.drawContours(overlap_source_host_fault_contours_image, overlap_source_host_fault_contours, -1, (0,255,0), 3)
    cv2.drawContours(overlap_source_host_inactive_fault_contours_image, overlap_source_host_inactive_fault_contours, -1, (0,255,0), 3)
    cv2.imwrite(m+'/'+m+'_'+t+'_overlap_fault.png', overlap_source_host_fault_contours_image)
    cv2.imwrite(m+'/'+m+'_'+t+'_overlap_inactive_fault.png', overlap_source_host_inactive_fault_contours_image)
    
    ###### Loop over active faults and check for overlap with source and host rock with shapely ######
    n_source_fault_overlaps = 0
    n_host_fault_overlaps = 0
    source_fault_overlaps = np.zeros(len(fault_contours))
    host_fault_overlaps = np.zeros(len(fault_contours))
    img_OFM12_contours = img_strainrate.copy()
    p = 0
    # Loop over each fault contour
    for contour in fault_contours:
      intersect_source = False
      intersect_host = False
      fault_polygon = Polygon()
      # Pad the fault polygon with user-set buffer
      if len(contour) > 2:
        fault_polygon = Polygon([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 2:
        fault_polygon = LineString([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 1:
        fault_polygon = Point(contour[0][0]).buffer(buffer)
      else:
        print ("Fault contour empty")
      # Loop over all source rock contours
      for source_contour in source_rock_contours:
        source_polygon = Polygon()
        # Pad the source polygon with user-set buffer
        if len(source_contour) > 2:
          source_polygon = Polygon([l[0] for l in source_contour]).buffer(buffer)
        # Create a line instead of a polygon
        elif len(source_contour) == 2:
          source_polygon = LineString([l[0] for l in source_contour]).buffer(buffer)
        # Create a point instead of a polygon
        elif len(source_contour) == 1:
          source_polygon = Point(contour[0][0]).buffer(buffer)
        else:
          print ("Source rock contour empty")
        # Check for overlap
        intersect_source = fault_polygon.intersects(source_polygon) 
        # Draw and count the overlap
        if intersect_source:
          cv2.drawContours(img_OFM12_contours, source_contour,-1,(0,255,0),3)
          n_source_fault_overlaps += 1
          source_fault_overlaps[p] += 1
        # Reset
        intersect_source = False

      # Loop over host contours
      for host_contour in host_rock_contours:
        host_polygon = Polygon()
        if len(host_contour) > 2:
          host_polygon = Polygon([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 2:
          host_polygon = LineString([l[0] for l in host_contour]).buffer(buffer)
        elif len(host_contour) == 1:
          host_polygon = Point(host_contour[0][0]).buffer(buffer)
        else:
          print ("Source rock contour empty")
        intersect_host = fault_polygon.intersects(host_polygon)
        if intersect_host:
          cv2.drawContours(img_OFM12_contours, host_contour,-1,(0,0,255),3)
          n_host_fault_overlaps += 1
          host_fault_overlaps[p] += 1
        # Reset
        intersect_host = False
      p += 1

    # Save and print output
    print("Number of source rock overlaps with active fault found automatically with shapely and buffer of", buffer, " = ", n_source_fault_overlaps)
    dataframe.loc[index_model_time, 'n_source_fault_overlaps'] = n_source_fault_overlaps
    print("Number of host rock overlaps with active fault found automatically with shapely and buffer of", buffer, " = ", n_host_fault_overlaps)
    dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = n_host_fault_overlaps

    # Check which fault overlaps with both source and host rock
    source_host_fault_overlaps = (source_fault_overlaps != 0) & (host_fault_overlaps != 0)
    print ("Number of OFM12s found automatically with Shapely: ", np.count_nonzero(source_host_fault_overlaps))
    dataframe.loc[index_model_time, 'n_OFM12'] = np.count_nonzero(source_host_fault_overlaps)
    
    ###### Save the OFM12 source and host on top of strainrate ######
    cv2.imwrite(m+'/'+m+'_'+t+'_OFM12.png', img_OFM12_contours)
    
    ###### Open the OFM12 image and ask user for n_OFM1 and n_OFM2 ######
    n_source = 0
    n_source_host = 0
    n_OFM1 = 0
    n_OFM2 = 0
    if len(source_rock_contours) > 0:
      # Ask user for interpretation
      if interactive and ((len(overlap_source_host_fault) > 0) or (np.count_nonzero(source_host_fault_overlaps) > 0)):
        cv2.imshow("Possible OFM1 and OFM2", img_OFM12_contours)
        cv2.imshow("Source, host, strainrate and strain", img)
        cv2.moveWindow("Source, host, strainrate and strain", 0, 250)
        cv2.imshow("Source, host, strainrate contours", overlap_source_host_fault_contours_image)
        cv2.moveWindow("Source, host, strainrate contours", 0, 500)
        cv2.imshow("All", img_all)
        cv2.moveWindow("All", 0, 750)
        cv2.waitKey(0)
        n_source = input("Nr of basins with source: ")
        n_source_host = input("Nr of basins with source and host: ")
        n_OFM1 = input("Nr of OFM1: ")
        n_OFM2 = input("Nr of OFM2: ")
        cv2.destroyWindow("Possible OFM1 and OFM2")
        cv2.destroyWindow("Source, host, strainrate and strain")
        cv2.destroyWindow("Source, host, strainrate contours")
        cv2.destroyWindow("All")
    dataframe.loc[index_model_time, 'n_source'] = n_source
    dataframe.loc[index_model_time, 'n_source_host'] = n_source_host
    dataframe.loc[index_model_time, 'n_OFM1'] = n_OFM1
    dataframe.loc[index_model_time, 'n_OFM2'] = n_OFM2
    print("Number of source rock overlaps with active fault found with shapely and buffer of", buffer, " = ", n_source_fault_overlaps)
    dataframe.loc[index_model_time, 'n_source_fault_overlaps'] = n_source_fault_overlaps
    print("Number of host rock overlaps with active fault found with shapely and buffer of", buffer, " = ", n_host_fault_overlaps)
    dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = n_host_fault_overlaps

    ###### Loop over inactive faults and check for each fault whether there is overlap with both source and host rock ######
    # If there is no overlap with source rock, skip checking host rock
    n_OFM3 = 0
    n_source_inactive_fault_overlaps = 0
    n_host_inactive_fault_overlaps = 0
    img_OFM3_contours = img_strain.copy()
    for contour in inactive_fault_contours:
      intersect_source = False
      intersect_host = False
      fault_polygon = Polygon()
      if len(contour) > 2:
        fault_polygon = Polygon([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 2:
        fault_polygon = LineString([l[0] for l in contour]).buffer(buffer)
      elif len(contour) == 1:
        fault_polygon = Point(contour[0][0]).buffer(buffer)
      else:
        print ("Fault contour empty")

      for source_contour in source_rock_contours:
        source_polygon = Polygon()
        if len(source_contour) > 2:
          source_polygon = Polygon([l[0] for l in source_contour]).buffer(buffer)
        elif len(source_contour) == 2:
          source_polygon = LineString([l[0] for l in source_contour]).buffer(buffer)
        elif len(source_contour) == 1:
          source_polygon = Point(source_contour[0][0]).buffer(buffer)
        else:
          print ("Source rock contour empty")

        intersect_source = fault_polygon.intersects(source_polygon) 
        if intersect_source:
          n_source_inactive_fault_overlaps += 1
          for host_contour in host_rock_contours:
            if len(host_contour) > 2:
              host_polygon = Polygon([l[0] for l in host_contour]).buffer(buffer)
            elif len(host_contour) == 2:
              host_polygon = LineString([l[0] for l in host_contour]).buffer(buffer)
            elif len(host_contour) == 1:
              host_polygon = Point(host_contour[0][0]).buffer(buffer)
            else:
              print ("Host rock contour empty")

            intersect_host = fault_polygon.intersects(host_polygon)
            if intersect_host:
              n_OFM3 += 1    
              cv2.drawContours(img_OFM3_contours, source_contour,-1,(0,255,0),2)
              cv2.drawContours(img_OFM3_contours, host_contour,-1,(0,0,255),2)
              # If we find one host rock area, then we stop looping over the rest
              break
          # If we have found source and host rock areas, then we stop looping over the source rock
          if intersect_host:
            break

    ###### Print and save data ######
    print ("Nr of OFM3s found automatically with Shapely: ", n_OFM3)
    dataframe.loc[index_model_time, 'n_OFM3'] = n_OFM3
    dataframe.loc[index_model_time, 'n_source_inactive_fault_overlaps'] = n_source_inactive_fault_overlaps

    ###### If requested, check OFM3s interactively ######
    # But only if there is a chance of OFM3
    if interactive and (n_OFM3 > 0 or len(overlap_source_host_inactive_fault) > 0):
      cv2.imshow("Possible OFM3", img_OFM3_contours)
      cv2.imshow("Source, host, strainrate and strain", img)
      cv2.moveWindow("Source, host, strainrate and strain", 0, 250)
      cv2.imshow("Source, host, strain contours", overlap_source_host_inactive_fault_contours_image)
      cv2.moveWindow("Source, host, strain contours", 0, 500)
      cv2.imshow("All", img_all)
      cv2.moveWindow("All", 0, 750)
      cv2.waitKey(0)
      n_OFM3 = input("Nr of OFM3: ")
      cv2.destroyWindow("Possible OFM3")
      cv2.destroyWindow("Source, host, strainrate and strain")
      cv2.destroyWindow("Source, host, strain contours")
      cv2.destroyWindow("All")

      print ("Nr of OFM3s found manually with Shapely: ", n_OFM3)
      dataframe.loc[index_model_time, 'n_OFM3'] = n_OFM3
    
    ###### Save the OFM3 source and host on top of strain ######
    cv2.imwrite(m+'/'+m+'_'+t+'_OFM3.png', img_OFM3_contours)
    
    ###### Update output file index ######
    index_model_time += 1
    
  ###### Write output file ######
  dataframe.to_csv(m+'/'+m+'_stats.csv',index=False)
