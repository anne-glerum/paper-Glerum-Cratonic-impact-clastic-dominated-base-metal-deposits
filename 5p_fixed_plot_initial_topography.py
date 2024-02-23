# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from matplotlib import rc
rc("pdf", fonttype=42)
rc("font", size=20)
rc("axes", titlesize=25)
rc("legend", fontsize=10)

# Model names
models = [
#          '5p_fixed_craton_UC23km_edge400000.0_sigma10000.0.txt',
#          '5p_fixed_craton_UC23km_edge450000.0_sigma10000.0.txt',
#          '5p_fixed_craton_UC23km_edge500000.0_sigma10000.0.txt',
          '5p_fixed_craton_UC23km_edge400000.0_sigma5000.0.txt',
          '5p_fixed_craton_UC23km_edge450000.0_sigma5000.0.txt',
          '5p_fixed_craton_UC23km_edge500000.0_sigma5000.0.txt',
         ]

output_name = '5p_fixed_comparison_sigma5_'

labels = [
#          '400 km, 10 km',
#          '450 km, 10 km',
#          '500 km, 10 km',
          '400 km, 5 km',
          '450 km, 5 km',
          '500 km, 5 km',
         ]

# Batlow
color1=[0.0051932, 0.098238, 0.34984]
color2=[0.063071, 0.24709, 0.37505]
color3=[0.10684, 0.34977, 0.38455]
color4=[0.23136, 0.4262, 0.33857]
color5=[0.40297, 0.48047, 0.24473]
color6=[0.60052, 0.5336, 0.17065]
color7=[0.81169, 0.57519, 0.25257]
color8=[0.96494, 0.62693, 0.46486]
color9=[0.99277, 0.70769, 0.71238]
color10=[0.98332, 0.79091, 0.95375]
colors = [
          color1, 
          color2, 
          color3, 
          color4, 
          color5, 
          color6, 
          color7, 
          color8, 
          color9, 
          color10, 
          color10, 
         ]

markers = [
           '|','x','','','','','','','','',''
          ]
dmark = 200

counter = 0
for m in models:
    with open(m) as f:
        x,topo = np.genfromtxt(f, comments='#', usecols=(0,1), delimiter=' ', unpack=True)
    plt.plot(x/1e3,topo,color=colors[counter],linestyle='solid',label=labels[counter],fillstyle='none',marker=markers[counter],markevery=dmark)

    counter += 1

# Labelling of plot
plt.xlabel("X [km]",weight="bold")
plt.ylabel(r"Topography [m]",weight="bold")
plt.legend(loc='upper left',ncol=2, columnspacing = 1.5)
plt.grid(axis='x',color='0.95')
plt.grid(axis='y',color='0.95')
plt.xlim(-7,707) # My
plt.ylim(-40., 440.) # km2
plt.tight_layout()

field='initial_topography_'
plt.savefig(output_name + '_CERI_' + str(field) + '.png',dpi=300,bbox_inches='tight')    
print ("Output in: ", output_name + '_CERI_' + str(field) + '.png')
