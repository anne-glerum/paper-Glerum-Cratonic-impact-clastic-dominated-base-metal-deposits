# Locate and count the number of dark green blobs
# in pngs that represent source rock.

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0/5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0_00029_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_280000_25000.png')  

# Make sure the image exists
assert img is not None, "File could not be read, check with os.path.exists()"

# Print the rows, columns and RGB/BGR channels of the image
print("Image rows, columns and channels:", img.shape)

# Build a mask where all dark green pixels are 255 and other colors are 0.
# The two tuples provide the lower and upper bounds for dark green (0,83,0).
source_rock = cv2.inRange(img, (0, 80, 0), (5, 86, 5))  

# Build a mask where all light green pixels are 255 and other colors are 0.
# The two tuples provide the lower and upper bounds in BGR.
host_rock_1 = cv2.inRange(img, (165, 217, 179), (171, 223, 185))  
host_rock_2 = cv2.inRange(img, (108, 187, 160), (114, 193, 166))  
host_rock_3 = cv2.inRange(img, (62, 132, 31), (68, 138, 37))  
tmp_host_rock = cv2.bitwise_or(host_rock_1,host_rock_2)
host_rock = cv2.bitwise_or(tmp_host_rock,host_rock_3)


# Subtract 1, because the background is counted.
n_source_rock = cv2.connectedComponents(source_rock)[0] - 1

# Retrieve the locations of the dark green pixels
locations = cv2.findNonZero(source_rock)

# Plot the thresholded image
#plt.imshow(source_rock,'gray',vmin=0,vmax=255)
#plt.imshow(host_rock,'gray',vmin=0,vmax=255)
plt.subplot(2,3,1),plt.imshow(source_rock,'gray',vmin=0,vmax=255)
plt.subplot(2,3,2),plt.imshow(host_rock,'gray',vmin=0,vmax=255)
plt.subplot(2,3,4),plt.imshow(host_rock_1,'gray',vmin=0,vmax=255)
plt.subplot(2,3,5),plt.imshow(host_rock_2,'gray',vmin=0,vmax=255)
plt.subplot(2,3,6),plt.imshow(host_rock_3,'gray',vmin=0,vmax=255)

plt.show()


# Print the number of green blobs identified
print(f'n_labels = {n_source_rock}')

