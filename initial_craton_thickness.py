# -*- coding: utf-8 -*-
"""
Created on Mon 14 Feb 2022 by Anne Glerum
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
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

# The depth at which the lithospheric pressure should be balanced
# between the normal lithosphere and the cratonic lithosphere
compensation_depth = 210e3 # m

# Lithostatic pressure (/g) at bottom of normal lithosphere
rho_z_normal_lithosphere = z_UC_normal*rho_UC_normal + z_LC_normal*rho_LC_normal + z_ML_normal*rho_ML_normal
print ("Rho*z normal lithosphere", rho_z_normal_lithosphere)

# Lithostatic pressure (/g) at bottom of perturbed lithosphere
rho_z_perturbed_lithosphere = z_UC_perturbed*rho_UC_perturbed + z_LC_perturbed*rho_LC_perturbed + z_ML_perturbed*rho_ML_perturbed
print ("Rho*z perturbed lithosphere", rho_z_perturbed_lithosphere)

# Assume normal continental lithosphere elevation is 0 m
# Lithostatic pressure (/g) at compensation depth for normal lithosphere
rho_z_normal = rho_z_normal_lithosphere + (compensation_depth - z_normal_lithosphere) * rho_asthenosphere
print ("Rho*z normal total", rho_z_normal)

# Lithostatic pressure (/g) at bottom of normal lithosphere
rho_z_craton_lithosphere = z_UC_craton*rho_UC_craton + z_LC_craton*rho_LC_craton + z_ML_craton*rho_ML_craton

print ("Rho*z craton lithosphere", rho_z_craton_lithosphere)

# The thickness of the asthenospheric layer underneath the craton
# required to balance the lithostatic pressure at the compensation depth
z_A_craton = (rho_z_normal - rho_z_craton_lithosphere) / rho_asthenosphere

print ("Asthenosphere thickness beneath craton", z_A_craton, "m")

# Compute craton elevation for a certain compensation depth
topo_craton = compensation_depth - z_craton_lithosphere - z_A_craton

print ("Positive topography craton", -topo_craton, "m")

# The thickness of the asthenospheric layer underneath the pertured lithosphere
# required to balance the lithostatic pressure at the compensation depth
z_A_perturbed = (rho_z_normal - rho_z_perturbed_lithosphere) / rho_asthenosphere

print ("Asthenosphere thickness beneath perturbed", z_A_perturbed, "m")

# Compute perturbed elevation for a certain compensation depth
topo_perturbed = compensation_depth - z_perturbed_lithosphere - z_A_perturbed

print ("Positive topography perturbed", -topo_perturbed, "m")
