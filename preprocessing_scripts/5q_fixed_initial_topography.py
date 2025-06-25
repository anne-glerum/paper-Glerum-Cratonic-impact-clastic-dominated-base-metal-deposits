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

base_file_name = "5q_fixed_craton_UC23km"

dx = 312.5
x_width = 700e3
x = np.arange(0,x_width+dx,dx)

topo_craton = 360 #m
topo_rift = 0 #1040 #m
topo_normal = 0 #m
rift_axis = 350e3 #m
craton_edge = 500e3 #m
sigma_craton = 5e3 #m
sigma_rift = 60e3 #m

# delete old file if it exists
total_file_name = base_file_name + "_edge" + str(craton_edge) + "_sigma" + str(sigma_craton) + ".txt"
file_exists = os.path.exists(total_file_name)
if file_exists:
  os.remove(total_file_name)

d_craton = x-craton_edge
d_rift = x-rift_axis
craton_contribution = ((0.5+0.5*np.tanh(d_craton/sigma_craton))*topo_craton) + ((0.5-0.5*np.tanh(d_craton/sigma_craton))*topo_normal)
rift_contribution = (1.0-topo_rift*np.exp(-(d_rift**2)/(2.0*(sigma_rift**2))))

topo = craton_contribution * rift_contribution

data = {'X': x, 'Topo': topo}

dataframe = pd.DataFrame(data=data)

print ("Dataframe: ", dataframe)

with open(total_file_name, 'a') as file:
    file.write('# POINTS: ' + str(int(x_width/dx)+1) + '\n')


# Write data to existing file
dataframe.to_csv(total_file_name,index=False, mode='a', header=False, sep=' ')
print ("Created " + total_file_name)
