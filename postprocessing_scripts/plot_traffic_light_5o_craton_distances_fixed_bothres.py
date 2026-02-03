# Initially based on https://matplotlib.org/stable/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py (or something similar),
# but later reduced to only showing solid color bars without the table. Therefore this script seems overly complicated.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as Axes
plt.rcParams["font.family"] = "Arial"
from matplotlib import rc
rc("xtick", labelsize= 10)
rc("ytick", labelsize= 10)
#rc("pdf", fonttype=42)
rc("font", size=12)
rc("axes", titlesize=25, labelsize=12)
rc("legend", fontsize=10)

output_name = "5o_fixed_sourcearea_hightrescomplete_cuttonewOS_stddev_"


# The average of the maximum source area [km2]
average_source_area = [
18.79,18.79,18.79,18.79,
8.83,8.83,8.83,8.83,
8.27,8.27,8.27,8.27,
9.421293,9.421293,9.421293,9.421293
]
# The standard devation of the maximum source area [km2]
average_source_area_stddev = [
4.36, 4.36, 4.36, 4.36,
6.71, 6.71, 6.71, 6.71,
3.66, 3.66, 3.66, 3.66,
3.49, 3.49, 3.49, 3.49
]

# The max of the average source area [km2]
max_average_source_area = [
18.10,18.10,18.10,18.10,
7.92,7.92,7.92,7.92,
6.82,6.82,6.82,6.82,
8.251289,8.251289,8.251289,8.251289,
]

# Analysis at every 0.5 My, cut to new OS
fav_basins = [
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
[5.56,3.78,2.11,1.67,3.89,2.78,1.44,1.33,4.0,3.0,1.44,2.11,4.22,3.78,1.89,1.67],
]
# Analysis at every 0.5 My, cuttonewOS
# n_source_max,n_source_host_max,n_OFM3_max,n_OFM12_max, stddev_n_source_max,stddev_n_source_host_max,stddev_n_OFM3_max,stddev_n_OFM12_max
# 400: 5.556,3.778,2.111,1.667, 0.707,0.876,0.789,0.675
# 450: 3.889,2.778,1.444,1.333, 1.364,0.972,0.882,0.500
# 500: 4.000,3.000,1.444,2.111, 0.707,1.000,0.726,0.601
#2000: 4.222,3.778,1.889,1.667, 0.833,0.972,0.782,0.707
fav_basins_stddevs = [
0.707,0.876,0.789,0.675,
1.364,0.972,0.882,0.500,
0.707,1.000,0.726,0.601,
0.833,0.972,0.782,0.707
]


# Analysis at every 0.5 My
#fav_basins = [
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#[5.56,3.89,2.22,1.67,3.89,2.78,1.56,1.33,4.0,3.0,1.44,2.11,4.33,3.78,1.89,1.667],
#]

# Analysis at every 2.5 My
#fav_basins = [
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#[4.89,3.56,2.0,1.0,3.22,1.89,1.11,0.78,3.67,2.67,1.33,1.11,3.56,2.67,1.78,1.0],
#]

# Old pp without python scripts (for craton runs including after OS):
#fav_basins = [
#[4,3,1,1,3,2,2,1,2,2,0,1,3,1,1,1],
#[5,3,2,1,4,1,1,1,3,2,1,1,4,2,2,0],
#[5,4,2,2,3,2,1,1,3,3,0,1,2,2,2,0],
#[3,3,2,2,3,1,0,0,2,2,1,1,2,2,1,1],
#[5,3,2,2,4,4,2,1,4,3,0,2,4,2,0,1],
#[5,3,2,1,2,2,0,1,3,3,1,1,5,2,1,1],
#[5,4,2,1,3,3,2,1,3,2,1,1,3,2,1,0],
#[5,3,2,1,2,1,1,0,6,4,3,2,3,3,3,0],
#[3,3,0,1,4,3,2,1,2,1,1,1,3,2,1,1],
#       ]

rift_types = ('50', '100', '150', 'inf')
columns = ('', '50', '', '', '', '100', '', '', '', '150', '', '', '', 'inf', '', '')

rift_types_locations = [2.5, 7.5, 12.5, 17.5]

rows = [
        '-1',
        '-2',
        '-3',
        '-4',
        '-5',
        '-6',
        '-7',
        '-8',
        '-9',
       ]

# Create dark green (source + host + active faults),
# green (source + host + inactive faults), orange (source + host)
# and red (source or host) color scales
colors_green = plt.cm.Greens(np.linspace(0, 0.5, len(rows)))
colors_darkgreen = plt.cm.Greens(np.linspace(0.5, 1.0, len(rows)))
colors_orange = plt.cm.Oranges(np.linspace(0, 0.5, len(rows)))
colors_red = plt.cm.Reds(np.linspace(0, 0.5, len(rows)))
n_rows = len(fav_basins)
n_cols = len(columns)

# Color for max average source area and its y-axis
color1=[0.0051932, 0.098238, 0.34984]
color2=[0.063071, 0.24709, 0.37505]
color3=[0.10684, 0.34977, 0.38455]
color4=[0.23136, 0.4262, 0.33857]
color7=[0.81169, 0.57519, 0.25257]
color8='blue'

# Color for the error bars
colors_ebar = [colors_red[5], colors_orange[5], colors_green[5], colors_darkgreen[3],
               colors_red[5], colors_orange[5], colors_green[5], colors_darkgreen[3],
               colors_red[5], colors_orange[5], colors_green[5], colors_darkgreen[3],
               colors_red[5], colors_orange[5], colors_green[5], colors_darkgreen[3]]

# The x-coordinate of the bars
index = np.arange(n_cols) + 0.5
index = [1.0,2.0,3.0,4.0,6.0,7.0,8.0,9.0,11.0,12.0,13.0,14.0,16,17,18,19]

# The width of each of the bars
bar_width = 1.0

# Initialize the vertical offset for the stacked bar chart.
y_offset = np.zeros(n_cols)

# Create two subplots on top of each other
# so that we can plot two different datasets
# in one graph
fig = plt.figure()
ax = fig.add_subplot(111, label = 'bars')
ax2 = fig.add_subplot(111, label = 'source', frame_on='False', sharex=ax)

ax.autoscale(enable=False)

# Plot bars and create text labels for the table
cell_text = []
counter = [0] * 9
for row in range(n_rows):
   
    #list_colors = [colors_red[counter[0]], colors_orange[counter[1]],colors_green[counter[2]],
    #               colors_red[counter[3]], colors_orange[counter[4]],colors_darkgreen[counter[5]],
    #               colors_red[counter[6]], colors_orange[counter[7]],colors_green[counter[8]]]
    list_colors = [colors_red[8], colors_orange[8],colors_green[8],colors_darkgreen[7],
                   colors_red[8], colors_orange[8],colors_green[8],colors_darkgreen[7],
                   colors_red[8], colors_orange[8],colors_green[8],colors_darkgreen[7],
                   colors_red[8], colors_orange[8],colors_green[8],colors_darkgreen[7]]
    #ax.bar(index, np.divide(fav_basins[row],9.), bar_width, bottom=y_offset, color=list_colors, align='center',tick_label=columns)
    rects = ax.bar(index, np.divide(fav_basins[row],9.), width=bar_width, bottom=y_offset, color=list_colors, align='center')
    if row == 8:
      for i, (rect, error, color) in enumerate(zip(rects, fav_basins_stddevs, colors_ebar)):
        ax.errorbar(rect.get_x() + rect.get_width()/2, np.divide(fav_basins[row],9.)[i]+y_offset[i], yerr=error, color=color, capsize=4, capthick=1)
#      ax.bar_label(rects, padding=3, fmt='%1.1f', fontsize=10)
    y_offset = y_offset + np.divide(fav_basins[row],9.)
    cell_text.append(['%1.1f' % (x) for x in fav_basins[row]])
    for b in range(9):
      if fav_basins[row][b] > 0:
        counter[b] += 1

total_basins_average = 7
ax.set_yticks(np.arange((int(np.max(total_basins_average)+2))))
ax.set_ylim=(0,int(np.max(total_basins_average)+1))

# Plot vertical lines separating the groups of three bars
ax.plot([5.0,5.0],[0,int(np.max(total_basins_average)+1)],color='0.75',linestyle='dashed')
ax.plot([10.0,10.0],[0,int(np.max(total_basins_average)+1)],color='0.75',linestyle='dashed')
ax.plot([15.0,15.0],[0,int(np.max(total_basins_average)+1)],color='0.75',linestyle='dashed')
# and horizontal grid lines
ax.set_axisbelow(True)
#ax.grid(axis='y',color='0.75')

# y-axis labeling
ax.set_ylabel("Average maximum number of basins", weight="bold")

# The formatting of the x-axis
ax.set_xlim(0., max(index)+1.0)
ax.set_xticks(rift_types_locations)
ax.set_xticklabels(rift_types)
ax.set_xlabel("Craton distance [km]", weight="bold")

# Plot title
#plt.title('Number of favorable basins per ICRD')

# Label the bars
ax.text(1.04,0.13,'source',rotation='vertical',ha='center',fontsize=8,color=colors_red[5])
ax.text(2.04,0.13,'source+host',rotation='vertical',ha='center',fontsize=8,color=colors_orange[5])
ax.text(3.04,0.13,'OFM3',rotation='vertical',ha='center',fontsize=8,color=colors_green[5])
ax.text(4.04,0.13,'OFM1+2',rotation='vertical',ha='center',fontsize=8,color=colors_darkgreen[3])
# Label the standard deviations
ax.text(1.04,6.32,r'$+\sigma$',rotation='horizontal',ha='center',fontsize=8,color=colors_red[5])
ax.text(1.04,4.67,r'$-\sigma$',rotation='horizontal',ha='center',fontsize=8,color=colors_red[5])
ax.text(4.04,4.69,r'$+\sigma$',rotation='horizontal',ha='center',fontsize=8,color=color8,alpha=0.2)
ax.text(4.04,2.70,r'$-\sigma$',rotation='horizontal',ha='center',fontsize=8,color=color8,alpha=0.2)

# Second subplot
# Transparent background
ax2.patch.set_facecolor('None')
#ax2.set_ylabel("Maximum average source area [km$\mathbf{^2}$]", color=color8, weight="bold")
ax2.set_ylabel("Average maximum source area [km$\mathbf{^2}$]", color=color8, weight="bold")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
ax2.tick_params(axis='y', color=color8, labelcolor=color8)
ax2.spines['right'].set_color(color8)
ax2.set_ylim(0,40)
ax2.set_yticks([0,10,20,30,40])

# Plot line indicating the average maximum source area per rift type
max_source_area_array = np.array(average_source_area)
#max_source_area_array = np.array(max_average_source_area)
max_source = max_source_area_array.max()
min_source = max_source_area_array.min()
# Create a second set of x-coordinates such that the line is
# constant over each set of three bars and then jumps
index_2 = [0, 1.5, 3, 5.0,
           5.0, 6.5, 7, 10.0, 
           10.0, 11.5, 13,15.0,
           15.0, 16.5, 18,20.0]
for column in range(n_cols): 
    ax2.fill_between(index_2, np.subtract(average_source_area,average_source_area_stddev), np.add(average_source_area,average_source_area_stddev),color=color8,alpha=0.005)
    ax2.plot(index_2, average_source_area,color=color8)
#    ax2.plot(index_2, max_average_source_area,color=color8)

field = 'traffic_light'
fig.savefig(output_name + '_CERI_' + field + '.png',bbox_inches='tight', dpi=300)    
print ('Figure in ', output_name + '_CERI_' + field + '.png')
