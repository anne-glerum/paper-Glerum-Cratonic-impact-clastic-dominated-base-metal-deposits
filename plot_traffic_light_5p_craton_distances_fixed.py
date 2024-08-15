import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as Axes
plt.rcParams["font.family"] = "Arial"
from matplotlib import rc
rc("xtick", labelsize= 15)
#rc("pdf", fonttype=42)
rc("font", size=15)
rc("axes", titlesize=25, labelsize=15)
rc("legend", fontsize=10)
#print (plt.rcParams.keys())

output_name = "5p_fixed_sourcearea_"


# The maximum average occurs before
# break-up
# The average of the maximum source area [km2]
average_source_area = [
18.98,18.98,18.98,18.98,
34.43,34.43,34.43,34.43,
18.25,18.25,18.25,18.25,
31.40, 31.40, 31.40, 31.40
]

# The max of the average source area
max_average_source_area = [
16.81,16.81,16.81,16.81,
31.85,31.85,31.85,31.85,
13.56,13.56,13.56,13.56,
29.80,29.80,29.80,29.80
]

# Only considering basins not in OSC
# 5p_fixed_surfPnorm_htanriftcraton_inittopo
fav_basins = [
[2,2,0,0,1,1,0,1,4,3,1,1,0,0,0,0],
[2,2,1,0,1,1,0,1,3,2,1,0,0,0,0,0],
[3,3,0,0,3,2,1,1,4,4,0,2,0,0,0,0],
[3,3,1,0,1,1,1,1,3,2,1,0,0,0,0,0],
[4,2,0,0,5,2,1,2,2,2,1,1,0,0,0,0],
[4,2,0,0,2,2,1,0,1,1,0,1,0,0,0,0],
[5,5,0,1,5,3,0,2,1,1,0,0,0,0,0,0],
[4,4,0,0,1,1,1,1,2,2,1,0,0,0,0,0],
[3,2,0,0,4,1,0,1,1,1,0,1,0,0,0,0],
       ]
# 5p_fixed_craton correct edge and surfPnorm
#fav_basins = [
#[2,2,0,0,1,1,0,1,4,3,1,1,0,0,0,0],
#[2,2,1,0,1,1,0,1,3,2,1,0,0,0,0,0],
#[3,3,0,0,3,2,1,1,4,4,0,2,0,0,0,0],
#[3,3,1,0,1,1,1,1,3,2,1,0,0,0,0,0],
#[4,2,0,0,5,2,1,2,2,2,1,1,0,0,0,0],
#[4,2,0,0,2,2,1,0,1,1,0,1,0,0,0,0],
#[5,5,0,1,5,3,0,2,1,1,0,0,0,0,0,0],
#[4,4,0,0,1,1,1,1,2,2,1,0,0,0,0,0],
#[3,2,0,0,4,1,0,1,1,1,0,1,0,0,0,0],
#       ]

rift_types = ('400', '450', '500', '550')
columns = ('', '400', '', '', '', '450', '', '', '', '500', '', '', '', '550', '', '')

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
print ("Darkgreen", colors_darkgreen[7])
print ("Green", colors_green[8])

# Color for max average source area and its y-axis
color1=[0.0051932, 0.098238, 0.34984]
color2=[0.063071, 0.24709, 0.37505]
color3=[0.10684, 0.34977, 0.38455]
color4=[0.23136, 0.4262, 0.33857]
color7=[0.81169, 0.57519, 0.25257]
color8='blue'

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
    rects = ax.bar(index, np.divide(fav_basins[row],9.), bar_width, bottom=y_offset, color=list_colors, align='center')
    if row == 8:
      ax.bar_label(rects, padding=3, fmt='%1.1f', fontsize=10)
    y_offset = y_offset + np.divide(fav_basins[row],9.)
    cell_text.append(['%1.1f' % (x) for x in fav_basins[row]])
    for b in range(9):
      if fav_basins[row][b] > 0:
        counter[b] += 1

total_basins_average = 4
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
ax.set_xlabel("Craton edge [km]", weight="bold")

# Plot title
#plt.title('Number of favorable basins per ICRD')

# Label the colors
#ax.text(6.0,1.2,'source',rotation='vertical',ha='center',fontsize=15)
#ax.text(7.0,1.2,'source and host',rotation='vertical',ha='center',fontsize=15)
#ax.text(8.0,1.2,'source, host, inactive fault',rotation='vertical',ha='center',fontsize=15)
#ax.text(9.0,1.2,'source, host, active fault',rotation='vertical',ha='center',fontsize=15)
ax.text(6.1,3.15,'S',rotation='vertical',ha='center',fontsize=15)
ax.text(7.1,3.15,'S+H',rotation='vertical',ha='center',fontsize=15)
ax.text(8.1,3.15,'S+H+IF',rotation='vertical',ha='center',fontsize=15)
ax.text(9.1,3.15,'S+H+AF',rotation='vertical',ha='center',fontsize=15)
#ax.legend(loc='upper left', ncol=1)

# Second subplot
# Transparent background
ax2.patch.set_facecolor('None')
ax2.set_ylabel("Maximum average source area [km$\mathbf{^2}$]", color=color8, weight="bold")
ax2.yaxis.tick_right()
ax2.yaxis.set_label_position('right') 
ax2.tick_params(axis='y', color=color8, labelcolor=color8)
ax2.spines['right'].set_color(color8)
ax2.set_ylim(0,35)
ax2.set_yticks([0,10,20,30])

# Plot line indicating the average maximum source area per rift type
#max_source_area_array = np.array(average_source_area)
max_source_area_array = np.array(max_average_source_area)
max_source = max_source_area_array.max()
min_source = max_source_area_array.min()
# Create a second set of x-coordinates such that the line is
# constant over each set of three bars and then jumps
index_2 = [0, 1.5, 3, 5.0,
           5.0, 6.5, 7, 10.0, 
           10.0, 11.5, 13,15.0,
           15.0, 16.5, 18,20.0]
for column in range(n_cols): 
#    ax2.plot(index_2, np.divide(average_source_area,1e6),color=color8)
    ax2.plot(index_2, max_average_source_area,color=color8)

field = 'traffic_light'
fig.savefig(output_name + '_CERI_' + field + '_noVHS_inactive_active.png',bbox_inches='tight', dpi=300)    
print ('Figure in ', output_name + '_CERI_' + field + '_noVHS_inactive_active.png')
