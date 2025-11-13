import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as Line
from scipy.io import netcdf
import numpy as np
import pandas as pd
from cmcrameri import cm

from cartopy import config
import cartopy.crs as ccrs

# This script plots global LAB thickness and the location
# of CD-type zinc-lead deposits based on the datafiles
# of Hoggard et al. 2020 (10.1038/s41561-020-0593-2).

# Path of the LAB thickness file. 
file_name_LAB = '../../../Literature/Hoggard_2020_Supplement_lithospheric_thickness_maps/SLNAAFSA.csv'
# Path of the deposit file.
file_name_deposits = '../../../Literature/Hoggard_2020_base_metal_deposit_compilation.xls'

##### LAB thickness #####
# Read LAB thickness and reformat the data
lon, lat, depth = np.genfromtxt(file_name_LAB, delimiter=", ", unpack=True)
# lon runs from 0 to 360 degrees with an interval of 0.5
# lat runs from 90 to -90 degrees with an interval of 0.5
lon_1D = lon[0:721]
lon_2D = lon.reshape(721,361)
lat_1D = lat[0:721*361:721]
depth = depth.reshape(361,721)

# Start a plot
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot the thickness data, colored for the 30-350 km interval. 
min_depth = 30 #km
max_depth = 350 #km
n_depth = 64
contour_levels = np.linspace(min_depth, max_depth, n_depth)
thickness_map = plt.contourf(lon_1D, lat_1D, depth, contour_levels, cmap=cm.acton_r,
             transform=ccrs.PlateCarree())
thickness_map.cmap.set_under('lime')
thickness_map.cmap.set_over('lime')

# Contour 170 km, as Hoggard et al. define this contour as the edge of cratons.
thickness_contour = plt.contour(lon_1D, lat_1D, depth, [170], colors=('white'), linewidths=(1,))

# Set up the color bar, shrink to plot height
cbar = plt.colorbar(thickness_map, shrink=0.545, ticks=[30,50,100,150,170,200,250,300,350], extend='both')
cbar.ax.set_ylabel('LAB depth [km]')
# Add the 170 contour line to the color bar
cbar.add_lines(thickness_contour)

##### Deposit locations #####
# Read location and age of deps and reformat the data
# The first sheet of the excel file contains the CD-type deposits,
# which is the default to read.
# The first row contains the column names.
column_names = ["Deposit", "Lon.", "Lat.", "Age (Ga)", "Total Zn+Pb (Mt)"]
df = pd.read_excel(file_name_deposits, usecols=column_names, na_values=["ND"])
print(df.head())

# Plot deposits with symbol size representing deposit size
# and symbol color representing Phanerozoic or Precambrian age.
min_size = df["Total Zn+Pb (Mt)"].min()
max_size = df["Total Zn+Pb (Mt)"].max()
df["Scaled Total Zn+Pb (Mt)"] = df["Total Zn+Pb (Mt)"].apply(lambda x: (((x - min_size) / (max_size - min_size)) * 10 + 2))
print(df.dtypes)
df["Color based on age"] = df["Age (Ga)"].apply(lambda x: ("yellow" if x < 0.541 else "orange"))
print(df.head())
print(df["Scaled Total Zn+Pb (Mt)"].min())
print(df["Scaled Total Zn+Pb (Mt)"].max())
print(len(df.index))

# zorder=10 used to place the scatter on top of all other items plotted
# except the lines to text
plt.scatter(df["Lon."], df["Lat."], s=df["Scaled Total Zn+Pb (Mt)"], color=df["Color based on age"], marker='o', edgecolors=None,
         transform=ccrs.PlateCarree(), zorder=10)

##### Other plot items #####
ax.coastlines(linewidths=(0.5,))
ax.text(145, -50, "Carpentaria", fontsize=6, rotation='horizontal', va='center', ha='center')
ax.text(-125, 30, "N-Am Cordillera", fontsize=6, rotation=-50, va='center', ha='center')
ax.plot([145, 140], [-46, -20], linestyle='solid', linewidth=0.5, color='black', marker='', transform=ccrs.PlateCarree(), zorder=11)
ax.plot([-122, -130], [33, 60], linestyle='solid', linewidth=0.5, color='black', marker='', transform=ccrs.PlateCarree(), zorder=11)
#ax.set_title('LAB depth contoured at 170 km')

##### Legend #####
# Create a legend for the coastlines.
legend_artists = [Line([0], [0], color='white', linewidth=1), 
                  Line([], [], color='yellow', marker='o', linestyle='None', markersize=3),
                  Line([], [], color='orange', marker='o', linestyle='None', markersize=3)]
legend_texts = ['craton edges', 'Phanerozoic deposits', 'Precambrian deposits']
legend = ax.legend(legend_artists, legend_texts, fancybox=True,
                       loc=(0.37,0.125), framealpha=0.75, fontsize=6, labelcolor='white')
legend.legendPatch.set_facecolor('grey')
legend.legendPatch.set_edgecolor('black')
legend.legendPatch.set_linewidth(0.5)

#plt.show()
plt.tight_layout()

# Save as pdf
output_filename = 'map_LAB_deposits.png'
plt.savefig(output_filename, dpi=300)
print ('Plot in: ' + output_filename)