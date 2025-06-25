# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import os
rc("pdf", fonttype=42)
rc("font", size=20)
rc("axes", titlesize=25)
rc("legend", fontsize=10)
# Scientific color maps
#from cmcrameri import cm
#from os.path import exists
#from pathlib import Path

# Path to models
base = r"/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"

# Normal lithosphere densities
rho_UC_normal = 2689.5 # kg/m3
rho_LC_normal = 2821 # kg/m3
rho_ML_normal = 3197.5 # kg/m3

# Normal lithosphere thicknesses
z_UC_normal = 20e3 # m
z_LC_normal = 15e3 # m
z_ML_normal = 85e3 # m
z_normal_lithosphere = z_UC_normal + z_LC_normal + z_ML_normal # m
print ("Thickness normal lithosphere", z_normal_lithosphere)

# Craton lithosphere densities
rho_UC_craton = 2692 # kg/m3
rho_LC_craton = 2825.5 # kg/m3
rho_ML_craton = 3203 #3163 # kg/m3
rho_asthenosphere = 3182 # kg/m3

# Craton lithosphere thicknesses
z_UC_craton = 23e3 # m
z_LC_craton = 20e3 # m
z_ML_craton = 157e3 # m
z_craton_lithosphere = z_UC_craton + z_LC_craton + z_ML_craton # m
print ("Thickness craton lithosphere", z_craton_lithosphere)

# Perturbed lithosphere densities
rho_UC_perturbed = 2686.15 # kg/m3
rho_LC_perturbed = 2812.2 # kg/m3
rho_ML_perturbed = 3191.8 # kg/m3

# Perturbed lithosphere thicknesses
z_UC_perturbed = 25e3 # m
z_LC_perturbed = 15e3 # m
z_ML_perturbed = 70e3 # m
z_perturbed_lithosphere = z_UC_perturbed + z_LC_perturbed + z_ML_perturbed # m

base_file_name = "5p_fixed_craton_UC23km"

dx = 312.5
x_width = 700e3
x = np.arange(0,x_width+dx,dx)

topo_craton = 360 #m
topo_rift = 0 #1040 #m
topo_normal = 0 #m
rift_axis = 350e3 #m
craton_edge = 350e3 #m
sigma_craton = 10e3 #m 
sigma_rift = 60e3 #m

# delete old file if it exists
total_file_name = base_file_name + "_litho_thicknesses_topo" + str(topo_craton) + "_edge" + str(craton_edge) + "_sigma" + str(sigma_craton) + ".txt"
file_exists = os.path.exists(total_file_name)
if file_exists:
  os.remove(total_file_name)

d_craton = x-craton_edge
d_rift = x-rift_axis

z_UC_craton_contribution =  ((0.5+0.5*np.tanh(d_craton/sigma_craton))*z_UC_craton) + ((0.5-0.5*np.tanh(d_craton/sigma_craton))*z_UC_normal)
z_LC_craton_contribution =  ((0.5+0.5*np.tanh(d_craton/sigma_craton))*z_LC_craton) + ((0.5-0.5*np.tanh(d_craton/sigma_craton))*z_LC_normal)
z_ML_craton_contribution =  ((0.5+0.5*np.tanh(d_craton/sigma_craton))*z_ML_craton) + ((0.5-0.5*np.tanh(d_craton/sigma_craton))*z_ML_normal)

z_UC_rift_contribution = (1.0-z_UC_perturbed*np.exp(-(d_rift**2)/(2.0*(sigma_rift**2))))
z_LC_rift_contribution = (1.0-z_LC_perturbed*np.exp(-(d_rift**2)/(2.0*(sigma_rift**2))))
z_ML_rift_contribution = (1.0-z_ML_perturbed*np.exp(-(d_rift**2)/(2.0*(sigma_rift**2))))

z_UC = z_UC_craton_contribution * z_UC_rift_contribution
z_LC = z_LC_craton_contribution * z_LC_rift_contribution
z_ML = z_ML_craton_contribution * z_ML_rift_contribution

data = {'X': x/1000, 'Thickness_UC': z_UC/1000, 'Thickness_LC': z_LC/1000, 'Thickness_ML': z_ML/1000, 'Thickness_L': (z_UC+z_LC+z_ML)/1000}

dataframe = pd.DataFrame(data=data)

with open(total_file_name, 'a') as file:
    file.write('# POINTS: ' + str(int(x_width/dx)+1) + '\n')
    file.write('# unit: km \n')


# Write data to existing file
dataframe.to_csv(total_file_name,index=False, mode='a', header=True, sep=' ', float_format='%.1f')
print ("Created " + total_file_name)

# Plot the data
plt.plot(x,z_UC),color=colors[0],linestyle='solid',label='Upper crust',fillstyle='none',marker=markers[counter],markevery=dmark)

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
