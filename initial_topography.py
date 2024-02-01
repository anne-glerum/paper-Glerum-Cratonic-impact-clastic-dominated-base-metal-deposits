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

base_file_name = "5p_fixed_craton_UC23km"

dx = 312.5
x_width = 700e3
x = np.arange(0,x_width+dx,dx)

topo_craton = 360 #450 #750 #m
topo_pert = 0 #1040 #m
topo_normal = 0 #m
rift_axis = 350e3 #m
craton_edge = 400e3 #m
sigma_polygon = 10e3 #m 
sigma_rift = 60e3 #m

# delete old file if it exists
total_file_name = base_file_name + "_edge" + str(craton_edge) + "_sigma" + str(sigma_polygon) + ".txt"
file_exists = os.path.exists(total_file_name)
if file_exists:
  os.remove(total_file_name)

topo = (1-np.exp(-((x-rift_axis)**2)/(2.0*(sigma_rift**2)))) *((0.5+0.5*np.tanh((x-craton_edge)/sigma_polygon))*topo_craton +(0.5-0.5*np.tanh((x-craton_edge)/sigma_polygon))*topo_normal)+(topo_pert * (np.exp(-((x-rift_axis)**2)/(2.0*(sigma_rift**2)))))

data = {'X': x, 'Topo': topo}

dataframe = pd.DataFrame(data=data)

print ("Dataframe: ", dataframe)

with open(total_file_name, 'a') as file:
    file.write('# POINTS: ' + str(int(x_width/dx)+1) + '\n')


# Write data to existing file
dataframe.to_csv(total_file_name,index=False, mode='a', header=False, sep=' ')
print ("Created " + total_file_name)
