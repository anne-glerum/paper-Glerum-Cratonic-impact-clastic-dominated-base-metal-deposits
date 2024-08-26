# Locate and count the number of dark green blobs
# in pngs that represent source rockn_source.

import cv2
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Polygon
import shapely
import itertools
import pandas as pd


# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"
base = r"/Users/acglerum/Documents/Postdoc/SG_SB/Projects/CERI_cratons/"

# Model names
models = [
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
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
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
]

###### Create dataframe to store output data ######
dataframe = pd.DataFrame(columns=['model_name','time','n_source','n_host','n_source_fault_overlaps','n_host_fault_overlaps','n_source_inactive_fault_overlaps', 'n_host_inactive_fault_overlaps'])
index_model_time = 0

# Create file paths
paths = [base+m for m in models]
ASPECT_time_steps = ['00029']
ASPECT_time_steps = ['00000','00001','00005','00010','00015','00020','00025','00030','00035','00040','00045','00050']

for m in models:
  for t in ASPECT_time_steps:

    # Read the input image
    img = cv2.imread(m+'/'+m+'_'+t+'_source_host_strain_strainrate_8_zoom2_280000_25000.png')
    
    img_source_host = cv2.imread(m+'/'+m+'_'+t+'_source_host_8_zoom2_280000_25000.png')  
    
    img_strainrate = cv2.imread(m+'/'+m+'_'+t+'_strainrate_8_zoom2_280000_25000.png')  
    
    img_strain = cv2.imread(m+'/'+m+'_'+t+'_plasticstrain_8_zoom2_280000_25000.png')  
    
    ###### Make sure the images exist ######
    assert img is not None, "File could not be read, check with os.path.exists()"
    assert img_source_host is not None, "File could not be read, check with os.path.exists()"
    assert img_strainrate is not None, "File could not be read, check with os.path.exists()"
    assert img_strain is not None, "File could not be read, check with os.path.exists()"
    
    ###### Print the rows, columns and RGB/BGR channels of the image ######
    print("Input image rows, columns and channels:", img.shape)
    print("Input image source host rows, columns and channels:", img_source_host.shape)
    print("Input image strainrate rows, columns and channels:", img_strainrate.shape)
    print("Input image plastic strain rows, columns and channels:", img_strain.shape)
    
    ###### Mask OFM ingredients ######
    # Build a mask where all dark green pixels are 255 and other colors are 0.
    # The two tuples provide the lower and upper bounds for dark green (0,85,0).
    source_rock = cv2.inRange(img_source_host, (0, 82, 0), (5, 88, 5))  
    
    # Build a mask where all light green pixels are 255 and other colors are 0.
    # Original RGBs:
    # Limestones 186 228 179
    # Carbonates 166 196 118
    # Silicates 35 139 69
    # The two tuples provide the lower and upper bounds in BGR.
    #host_rock_1 = cv2.inRange(img_source_host, (176, 225, 183), (182, 231, 189))  
    #host_rock_2 = cv2.inRange(img_source_host, (115, 193, 163), (115, 199, 169))  
    #host_rock_3 = cv2.inRange(img_source_host, (66, 136, 32), (782, 142, 38))  
    host_rock_1 = cv2.inRange(img, (165, 217, 179), (171, 223, 185))  
    host_rock_2 = cv2.inRange(img, (108, 187, 160), (114, 193, 166))  
    host_rock_3 = cv2.inRange(img, (62, 132, 31), (68, 138, 37))
    # Combine the three different host rocks into one.
    tmp_host_rock = cv2.bitwise_or(host_rock_1,host_rock_2)
    host_rock = cv2.bitwise_or(tmp_host_rock,host_rock_3)
    
    # Build a mask where all black pixels are 255 and other colors are 0.
    # The two tuples provide the lower and upper bounds for black (0,0,0).
    active_fault_zone = cv2.inRange(img_strainrate, (0, 0, 0), (220, 220, 220))  
    
    # Build a mask where all grey pixels are 255 and other colors are 0.
    # The two tuples provide the lower and upper bounds for greys.
    inactive_fault_zone = cv2.inRange(img_strain, (0, 0, 0), (230, 230, 230))
    
    ###### Check for overlaps ######
    overlap_source_fault = cv2.bitwise_and(source_rock, active_fault_zone)
    overlap_host_fault = cv2.bitwise_and(host_rock, active_fault_zone)
    overlap_source_inactive_fault = cv2.bitwise_and(source_rock, inactive_fault_zone)
    overlap_host_inactive_fault = cv2.bitwise_and(host_rock, inactive_fault_zone)
    overlap_source_host_fault = cv2.bitwise_or(overlap_source_fault, overlap_host_fault)
    overlap_source_host_inactive_fault = cv2.bitwise_or(overlap_source_inactive_fault, overlap_host_inactive_fault)
    
    ###### Get contours of overlaps ######
    overlap_source_fault_contours, overlap_source_fault_hierarchy = cv2.findContours(overlap_source_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock overlaps with active fault found = " + str(len(overlap_source_fault_contours)))
    dataframe.loc[index_model_time, 'n_source_fault_overlaps'] = len(overlap_source_fault_contours)
    
    overlap_source_inactive_fault_contours, overlap_source_inactive_fault_hierarchy = cv2.findContours(overlap_source_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock overlaps with inactive fault found = " + str(len(overlap_source_inactive_fault_contours)))
    dataframe.loc[index_model_time, 'n_source_inactive_fault_overlaps'] = len(overlap_source_inactive_fault_contours)
    
    overlap_host_fault_contours, overlap_host_fault_hierarchy = cv2.findContours(overlap_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of host rock overlaps with active fault found = " + str(len(overlap_host_fault_contours)))
    dataframe.loc[index_model_time, 'n_host_fault_overlaps'] = len(overlap_host_fault_contours)
    
    overlap_host_inactive_fault_contours, overlap_host_inactive_fault_hierarchy = cv2.findContours(overlap_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of host rock overlaps with inactive fault found = " + str(len(overlap_host_inactive_fault_contours)))
    dataframe.loc[index_model_time, 'n_host_inactive_fault_overlaps'] = len(overlap_host_inactive_fault_contours)
    
    overlap_source_host_fault_contours, overlap_source_host_fault_hierarchy = cv2.findContours(overlap_source_host_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    overlap_source_host_inactive_fault_contours, overlap_source_host_inactive_fault_hierarchy = cv2.findContours(overlap_source_host_inactive_fault, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    ###### Get contours of individual OFM elements ######
    # Get the contours of source rock area
    source_rock_contours, source_rock_hierarchy = cv2.findContours(source_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print("Number of source rock contours found = " + str(len(source_rock_contours)))
    dataframe.loc[index_model_time, 'n_source'] = len(source_rock_contours)
    
    # Get the contours of host rock area
    host_rock_contours, host_rock_hierarchy = cv2.findContours(host_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    dataframe.loc[index_model_time, 'n_host'] = len(host_rock_contours)
    
    # Get the contours of active fault zone area
    fault_contours, fault_hierarchy = cv2.findContours(active_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #print("Number of fault rock contours found = " + str(len(fault_contours)))
    
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
    
    ####### Add bounding box or circle around contours ######
    ## TODO improve on dtype=object
    ## Bounding circle source rock areas
    #source_rock_bounding_image = cv2.cvtColor(source_rock.copy(), cv2.COLOR_GRAY2RGB)
    #source_rock_bounding_circle_centers = np.full(len(source_rock_contours), 0., dtype='i,i')
    #source_rock_bounding_circle_radii = np.full(len(source_rock_contours), 0., dtype='i')
    #source_rock_bounding_rectangle = np.empty(len(source_rock_contours),dtype=object)
    #for i, i_source_rock_contours in enumerate(source_rock_contours):
    #  (x_source_rock,y_source_rock),radius_source_rock = cv2.minEnclosingCircle(i_source_rock_contours)
    #  source_rock_bounding_circle_centers[i] = (int(x_source_rock),int(y_source_rock))
    #  source_rock_bounding_circle_radii[i] = int(radius_source_rock)
    #  cv2.circle(source_rock_bounding_image,source_rock_bounding_circle_centers[i],source_rock_bounding_circle_radii[i],(0,255,0),2)
    #
    #  area = cv2.contourArea(i_source_rock_contours)
    #  if (area > 0):
    #    source_rectangle = cv2.minAreaRect(i_source_rock_contours)
    #    source_rock_bounding_rectangle[i] = source_rectangle
    #
    ## Bounding circle host rock areas
    #host_rock_bounding_image = cv2.cvtColor(host_rock.copy(), cv2.COLOR_GRAY2RGB)
    #host_rock_bounding_circle_centers = np.full(len(host_rock_contours), 0., dtype='i,i')
    #host_rock_bounding_circle_radii = np.full(len(host_rock_contours), 0., dtype='i')
    #host_rock_bounding_rectangle = np.empty(len(host_rock_contours),dtype=object)
    #for i, i_host_rock_contours in enumerate(host_rock_contours):
    #  (x_host_rock,y_host_rock),radius_host_rock = cv2.minEnclosingCircle(i_host_rock_contours)
    #  host_rock_bounding_circle_centers[i] = (int(x_host_rock),int(y_host_rock))
    #  host_rock_bounding_circle_radii[i] = int(radius_host_rock)
    #  cv2.circle(host_rock_bounding_image,host_rock_bounding_circle_centers[i],host_rock_bounding_circle_radii[i],(0,255,0),2)
    #
    #  area = cv2.contourArea(i_host_rock_contours)
    #  if (area > 0):
    #    host_rectangle = cv2.minAreaRect(i_host_rock_contours)
    #    host_rock_bounding_rectangle[i] = host_rectangle
    #
    ## Bounding circle and rotating box active fault areas
    #fault_bounding_image = cv2.cvtColor(active_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    #fault_bounding_circle_centers = np.full(len(fault_contours), 0., dtype='i,i')
    #fault_bounding_circle_radii = np.full(len(fault_contours), 0., dtype='i')
    #fault_bounding_rectangle = np.empty(len(fault_contours),dtype=object)
    #for i, i_fault_contours in enumerate(fault_contours):
    #  (x_fault,y_fault),radius_fault = cv2.minEnclosingCircle(i_fault_contours)
    #  fault_bounding_circle_centers[i] = (int(x_fault),int(y_fault))
    #  fault_bounding_circle_radii[i] = int(radius_fault)
    #  #cv2.circle(fault_bounding_image,fault_bounding_circle_centers[i],fault_bounding_circle_radii[i],(0,255,0),2)
    #
    #  area = cv2.contourArea(i_fault_contours)
    #  print ("Area: ", area)
    #  if (area > 5):
    #    fault_rectangle = cv2.minAreaRect(i_fault_contours)
    #    fault_bounding_rectangle[i] = fault_rectangle
    #    fault_box = cv2.boxPoints(fault_rectangle)
    #    fault_box = np.int0(fault_box)
    #    print ("Fault box coordinates: ", fault_box)
    #    cv2.drawContours(fault_bounding_image,[fault_box],0,(0,255,0),2)
    #
    ## Bounding circle inactive fault areas
    #inactive_fault_bounding_image = cv2.cvtColor(inactive_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
    #inactive_fault_bounding_circle_centers = np.full(len(inactive_fault_contours), 0., dtype='i,i')
    #inactive_fault_bounding_circle_radii = np.full(len(inactive_fault_contours), 0., dtype='i')
    #inactive_fault_bounding_rectangle = np.empty(len(inactive_fault_contours),dtype=object)
    #for i, i_inactive_fault_contours in enumerate(inactive_fault_contours):
    #  (x_inactive_fault,y_inactive_fault),radius_inactive_fault = cv2.minEnclosingCircle(i_inactive_fault_contours)
    #  inactive_fault_bounding_circle_centers[i] = (int(x_inactive_fault),int(y_inactive_fault))
    #  inactive_fault_bounding_circle_radii[i] = int(radius_inactive_fault)
    #  #cv2.circle(inactive_fault_bounding_image,inactive_fault_bounding_circle_centers[i],inactive_fault_bounding_circle_radii[i],(0,255,0),2)
    #
    #  area = cv2.contourArea(i_inactive_fault_contours)
    #  if (area > 0):
    #    inactive_fault_rectangle = cv2.minAreaRect(i_inactive_fault_contours)
    #    inactive_fault_bounding_rectangle[i] = inactive_fault_rectangle
    #    inactive_fault_box = cv2.boxPoints(inactive_fault_rectangle)
    #    inactive_fault_box = np.int0(inactive_fault_box)
    #    #print ("Fault box coordinates: ", inactive_fault_box)
    #    cv2.drawContours(inactive_fault_bounding_image,[inactive_fault_box],0,(0,255,0),2)
    ####### Output number of relevant contours ######
    #
    #
    ####### Loop over faults and check overlap ######
    #fault_source_intersections = []
    #fault_host_intersections = []
    #for i,i_fault_rectangle in enumerate(fault_bounding_rectangle):
    #  for j,j_source_rectangle in enumerate(source_rock_bounding_rectangle):
    #    intersecting, intersection = (cv2.rotatedRectangleIntersection(i_fault_rectangle, j_source_rectangle))
    #    if intersecting:
    #      # drawContours expects integers, so convert floats to ints
    #      fault_source_intersections.append(intersection.astype(np.int32))
    #  for p,j_host_rectangle in enumerate(host_rock_bounding_rectangle):
    #    intersecting, intersection = (cv2.rotatedRectangleIntersection(i_fault_rectangle, j_host_rectangle))
    #    if intersecting:
    #      # drawContours expects integers, so convert floats to ints
    #      fault_host_intersections.append(intersection.astype(np.int32))
    #fault_source_intersections = np.asarray(fault_source_intersections)
    #fault_host_intersections = np.asarray(fault_host_intersections)
    
    ###### Loop over inactive faults and check for each fault whether there is overlap with both source and host rock ######
    n_OFM3 = 0
    img_OFM3_contours = img_strain.copy()
    for contour in inactive_fault_contours:
      area = cv2.contourArea(contour)
      if (area > 0):
        intersect_source = False
        intersect_host = False
        fault_polygon = Polygon([l[0] for l in contour])
        for source_contour in source_rock_contours:
          source_area = cv2.contourArea(source_contour)
          if source_area > 0:
            source_polygon = Polygon([l[0] for l in source_contour]).buffer(2)
            intersect_source = fault_polygon.intersects(source_polygon) 
            if intersect_source:
              for host_contour in host_rock_contours:
                host_area = cv2.contourArea(host_contour)
                if host_area > 0:
                  host_polygon = Polygon([l[0] for l in host_contour]).buffer(2)
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
    print ("Nr of OFM3s: ", n_OFM3)
    
    ###### Save the OFM3 source and host on top of strain ######
    cv2.imwrite(m+'/'+m+'_'+t+'_OFM3.png', img_OFM3_contours)
    
    
    ####### Save the outlines of the overlaps on the original image ######
    #intersection_image = img.copy()
    ##for fault_source_intersection in fault_source_intersections:
    #if (len(fault_source_intersections) > 0):
    #  cv2.drawContours(intersection_image,fault_source_intersections,-1,(0,255,0),2)
    ##if (len(fault_host_intersections) > 0):
    ##  cv2.drawContours(intersection_image,fault_host_intersections,-1,(0,0,255),2)
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_intersections.png', intersection_image)
      
    ###### Save the source and host contours on the original image ######
    # This function modifies the input image, so we make a copy.
    # We also have to change this single channel copy to a 3 channel image.
    #source_host_rock_contours_image = img.copy()
    #cv2.drawContours(source_host_rock_contours_image, source_rock_contours, -1, (0,255,0), 3)
    #cv2.drawContours(source_host_rock_contours_image, host_rock_contours, -1, (0,0,255), 3)
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_contours.png', source_host_rock_contours_image)
    
    ###### Plot the strainrate and strain contours on the original image ######
    # This function modifies the input image, so we make a copy.
    # We also have to change this single channel copy to a 3 channel image.
    #strainrate_contours_image = img_strainrate.copy()
    #cv2.drawContours(strainrate_contours_image, fault_contours, -1, (0,255,0), 3)
    #strain_contours_image = img_strain.copy()
    #cv2.drawContours(strain_contours_image, inactive_fault_contours, -1, (0,0,255), 3)
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate_contours.png', strainrate_contours_image)
    
    ###### Output information ######
    # Subtract 1, because the background is counted.
    #n_source_rock = cv2.connectedComponents(source_rock)[0] - 1
    #n_host_rock = cv2.connectedComponents(host_rock)[0] - 1
    # Print the number of green blobs identified
    #print(f'Number of source rock areas: {n_source_rock}')
    #print(f'Number of host rock areas: {n_host_rock}')
    #print(f'Number of source rock areas connected to faults:', len(fault_source_intersections))
    #print(f'Number of host rock areas connected to faults:', len(fault_host_intersections))
    
    ###### Write output file ######
    dataframe.to_csv(m+'/'+m+'_'+t+'_stats.csv',index=False)
    
    
    # Write images to file
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain_contours.png', strain_contours_image)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_rock.png', source_rock)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_host_rock.png', host_rock)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate.png', active_fault_zone)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain.png', inactive_fault_zone)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate_bounding_boxes.png', fault_bounding_image)
    
    #cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain_bounding_boxes.png', inactive_fault_bounding_image)
