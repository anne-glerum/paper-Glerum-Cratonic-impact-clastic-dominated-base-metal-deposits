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
thresh = cv2.inRange(img, (0, 80, 0), (5, 86, 5))  

#dilated_thresh = cv2.dilate(thresh, np.ones((3, 3), np.uint8))  # Dilate thresh because the blobs has green border that splits small blobs

# Subtract 1, because the background is counted.
n_labels = cv2.connectedComponents(thresh)[0] - 1

# Retrieve the locations of the dark green pixels
locations = cv2.findNonZero(thresh)

# Print the number of green blobs identified
print(f'n_labels = {n_labels}')

