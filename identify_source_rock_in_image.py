# Locate and count the number of dark green blobs
# in pngs that represent source rock.

import cv2
import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Polygon
import shapely
import itertools

# Read the input image
img = cv2.imread('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_host_strain_strainrate_8_zoom2_280000_25000.png')

img_source_host = cv2.imread('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_host_8_zoom2_280000_25000.png')  

img_strainrate = cv2.imread('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate_8_zoom2_280000_25000.png')  

img_strain = cv2.imread('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_plasticstrain_8_zoom2_280000_25000.png')  

# Make sure the images exist
assert img is not None, "File could not be read, check with os.path.exists()"
assert img_source_host is not None, "File could not be read, check with os.path.exists()"
assert img_strainrate is not None, "File could not be read, check with os.path.exists()"
assert img_strain is not None, "File could not be read, check with os.path.exists()"

# Print the rows, columns and RGB/BGR channels of the image
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
active_fault_zone = cv2.inRange(img_strainrate, (0, 0, 0), (240, 240, 240))  

# Build a mask where all grey pixels are 255 and other colors are 0.
# The two tuples provide the lower and upper bounds for greys.
inactive_fault_zone = cv2.inRange(img_strain, (0, 0, 0), (230, 230, 230))

###### Get contours ######
# Get the contours of source rock area
#source_rock_contours, source_rock_hierarchy = cv2.findContours(source_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
source_rock_contours, source_rock_hierarchy = cv2.findContours(source_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of source rock Contours found = " + str(len(source_rock_contours)))

# Get the contours of host rock area
host_rock_contours, host_rock_hierarchy = cv2.findContours(host_rock, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of host rock Contours found = " + str(len(host_rock_contours)))

# Get the contours of active fault zone area
fault_contours, fault_hierarchy = cv2.findContours(active_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of fault rock Contours found = " + str(len(fault_contours)))

# Get the contours of inactive fault zone area
inactive_fault_contours, inactive_fault_hierarchy = cv2.findContours(inactive_fault_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

###### Add bounding box or circle around contours ######
# TODO improve on dtype=object
# Bounding circle source rock areas
source_rock_bounding_image = cv2.cvtColor(source_rock.copy(), cv2.COLOR_GRAY2RGB)
source_rock_bounding_circle_centers = np.full(len(source_rock_contours), 0., dtype='i,i')
source_rock_bounding_circle_radii = np.full(len(source_rock_contours), 0., dtype='i')
source_rock_bounding_rectangle = np.empty(len(source_rock_contours),dtype=object)
for i, i_source_rock_contours in enumerate(source_rock_contours):
  (x_source_rock,y_source_rock),radius_source_rock = cv2.minEnclosingCircle(i_source_rock_contours)
  source_rock_bounding_circle_centers[i] = (int(x_source_rock),int(y_source_rock))
  source_rock_bounding_circle_radii[i] = int(radius_source_rock)
  cv2.circle(source_rock_bounding_image,source_rock_bounding_circle_centers[i],source_rock_bounding_circle_radii[i],(0,255,0),2)

  area = cv2.contourArea(i_source_rock_contours)
  if (area > 0):
    source_rectangle = cv2.minAreaRect(i_source_rock_contours)
    source_rock_bounding_rectangle[i] = source_rectangle

# Bounding circle host rock areas
host_rock_bounding_image = cv2.cvtColor(host_rock.copy(), cv2.COLOR_GRAY2RGB)
host_rock_bounding_circle_centers = np.full(len(host_rock_contours), 0., dtype='i,i')
host_rock_bounding_circle_radii = np.full(len(host_rock_contours), 0., dtype='i')
host_rock_bounding_rectangle = np.empty(len(host_rock_contours),dtype=object)
for i, i_host_rock_contours in enumerate(host_rock_contours):
  (x_host_rock,y_host_rock),radius_host_rock = cv2.minEnclosingCircle(i_host_rock_contours)
  host_rock_bounding_circle_centers[i] = (int(x_host_rock),int(y_host_rock))
  host_rock_bounding_circle_radii[i] = int(radius_host_rock)
  cv2.circle(host_rock_bounding_image,host_rock_bounding_circle_centers[i],host_rock_bounding_circle_radii[i],(0,255,0),2)

  area = cv2.contourArea(i_host_rock_contours)
  if (area > 0):
    host_rectangle = cv2.minAreaRect(i_host_rock_contours)
    host_rock_bounding_rectangle[i] = host_rectangle

# Bounding circle and rotating box active fault areas
fault_bounding_image = cv2.cvtColor(active_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
fault_bounding_circle_centers = np.full(len(fault_contours), 0., dtype='i,i')
fault_bounding_circle_radii = np.full(len(fault_contours), 0., dtype='i')
fault_bounding_rectangle = np.empty(len(fault_contours),dtype=object)
for i, i_fault_contours in enumerate(fault_contours):
  (x_fault,y_fault),radius_fault = cv2.minEnclosingCircle(i_fault_contours)
  fault_bounding_circle_centers[i] = (int(x_fault),int(y_fault))
  fault_bounding_circle_radii[i] = int(radius_fault)
  #cv2.circle(fault_bounding_image,fault_bounding_circle_centers[i],fault_bounding_circle_radii[i],(0,255,0),2)

  area = cv2.contourArea(i_fault_contours)
  print ("Area: ", area)
  if (area > 5):
    fault_rectangle = cv2.minAreaRect(i_fault_contours)
    fault_bounding_rectangle[i] = fault_rectangle
    fault_box = cv2.boxPoints(fault_rectangle)
    fault_box = np.int0(fault_box)
    print ("Fault box coordinates: ", fault_box)
    cv2.drawContours(fault_bounding_image,[fault_box],0,(0,255,0),2)

# Bounding circle inactive fault areas
inactive_fault_bounding_image = cv2.cvtColor(inactive_fault_zone.copy(), cv2.COLOR_GRAY2RGB)
inactive_fault_bounding_circle_centers = np.full(len(inactive_fault_contours), 0., dtype='i,i')
inactive_fault_bounding_circle_radii = np.full(len(inactive_fault_contours), 0., dtype='i')
inactive_fault_bounding_rectangle = np.empty(len(inactive_fault_contours),dtype=object)
for i, i_inactive_fault_contours in enumerate(inactive_fault_contours):
  (x_inactive_fault,y_inactive_fault),radius_inactive_fault = cv2.minEnclosingCircle(i_inactive_fault_contours)
  inactive_fault_bounding_circle_centers[i] = (int(x_inactive_fault),int(y_inactive_fault))
  inactive_fault_bounding_circle_radii[i] = int(radius_inactive_fault)
  #cv2.circle(inactive_fault_bounding_image,inactive_fault_bounding_circle_centers[i],inactive_fault_bounding_circle_radii[i],(0,255,0),2)

  area = cv2.contourArea(i_inactive_fault_contours)
  if (area > 0):
    inactive_fault_rectangle = cv2.minAreaRect(i_inactive_fault_contours)
    inactive_fault_bounding_rectangle[i] = inactive_fault_rectangle
    inactive_fault_box = cv2.boxPoints(inactive_fault_rectangle)
    inactive_fault_box = np.int0(inactive_fault_box)
    #print ("Fault box coordinates: ", inactive_fault_box)
    cv2.drawContours(inactive_fault_bounding_image,[inactive_fault_box],0,(0,255,0),2)
###### Output number of relevant contours ######
print("Number of inactive_fault rock Contours found = " + str(len(inactive_fault_bounding_rectangle)))



###### Loop over faults and check overlap ######
fault_source_intersections = []
fault_host_intersections = []
for i,i_fault_rectangle in enumerate(fault_bounding_rectangle):
  for j,j_source_rectangle in enumerate(source_rock_bounding_rectangle):
    intersecting, intersection = (cv2.rotatedRectangleIntersection(i_fault_rectangle, j_source_rectangle))
    if intersecting:
      # drawContours expects integers, so convert floats to ints
      fault_source_intersections.append(intersection.astype(np.int32))
  for p,j_host_rectangle in enumerate(host_rock_bounding_rectangle):
    intersecting, intersection = (cv2.rotatedRectangleIntersection(i_fault_rectangle, j_host_rectangle))
    if intersecting:
      # drawContours expects integers, so convert floats to ints
      fault_host_intersections.append(intersection.astype(np.int32))
fault_source_intersections = np.asarray(fault_source_intersections)
fault_host_intersections = np.asarray(fault_host_intersections)

###### Plot the outlines of the overlaps on the original image ######
intersection_image = img.copy()
#for fault_source_intersection in fault_source_intersections:
if (len(fault_source_intersections) > 0):
  cv2.drawContours(intersection_image,fault_source_intersections,-1,(0,255,0),2)
if (len(fault_host_intersections) > 0):
  cv2.drawContours(intersection_image,fault_host_intersections,-1,(0,0,255),2)
  
###### Plot the source and host contours on the original image ######
# This function modifies the input image, so we make a copy.
# We also have to change this single channel copy to a 3 channel image.
source_host_rock_contours_image = img.copy()
cv2.drawContours(source_host_rock_contours_image, source_rock_contours, -1, (0,255,0), 3)
cv2.drawContours(source_host_rock_contours_image, host_rock_contours, -1, (0,0,255), 3)

###### Plot the strainrate and strain contours on the original image ######
# This function modifies the input image, so we make a copy.
# We also have to change this single channel copy to a 3 channel image.
#strainrate_strain_contours_image = img.copy()
strainrate_contours_image = img_strainrate.copy()
cv2.drawContours(strainrate_contours_image, fault_contours, -1, (0,255,0), 3)
strain_contours_image = img_strain.copy()
cv2.drawContours(strain_contours_image, inactive_fault_contours, -1, (0,0,255), 3)

###### Output information ######
# Subtract 1, because the background is counted.
n_source_rock = cv2.connectedComponents(source_rock)[0] - 1
n_host_rock = cv2.connectedComponents(host_rock)[0] - 1
# Print the number of green blobs identified
print(f'Number of source rock areas: {n_source_rock}')
print(f'Number of host rock areas: {n_host_rock}')
print(f'Number of source rock areas connected to faults:', len(fault_source_intersections))
print(f'Number of host rock areas connected to faults:', len(fault_host_intersections))


# Write images to file
cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_intersections.png', intersection_image)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_contours.png', source_host_rock_contours_image)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate_contours.png', strainrate_contours_image)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain_contours.png', strain_contours_image)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_source_rock.png', source_rock)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_host_rock.png', host_rock)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate.png', active_fault_zone)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain.png', inactive_fault_zone)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strainrate_bounding_boxes.png', fault_bounding_image)

cv2.imwrite('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_strain_bounding_boxes.png', inactive_fault_bounding_image)
