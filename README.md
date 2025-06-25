This repository belongs to the paper

*Cratonic impact on clastic-dominated base metal deposits in continental rifts*

by

Glerum, A.
Brune, S.,
Magnall, J. M.,
Weis, P. and
Gleeson, S. A.

currently under review.

# Documentation
The numerical simulations presented in this paper were run with the geodynamics code ASPECT ([https://aspect.geodynamics.org/](https://aspect.geodynamics.org/)) coupled to the surface processes code FastScape ([https://fastscape.org/fastscapelib-fortran/](https://fastscape.org/fastscapelib-fortran/)).


## ASPECT version
The ASPECT input files provided in this repository correspond to commit e5d8d53b65705abf1f328eb918c9e2ac41d26d53 of the ASPECT branch 
34a1b89fe

[https://github.com/anne-glerum/aspect/tree/FastScapeASPECT](https://github.com/anne-glerum/aspect/tree/FastScapeASPECT)

This branch is built on commit 84d40e745328f62df1a09e15a9f1bb4fdc86141a of the ASPECT 2.4.0-pre development branch,
which can be found at [https://github.com/geodynamics/aspect](https://github.com/geodynamics/aspect). 
A copy of e5d8d53 can be found in the folder /src_ASPECT of Zenodo archive https://doi.org/10.5281/zenodo.10048075.
Note that the commit file reported in the ASPECT output file log.txt differs from the above commit number because of an additional merge commit.

## Additional ASPECT plugins
For the initial model conditions, we used the ASPECT plugins in the folder /plugins of Zenodo archive https://doi.org/10.5281/zenodo.10048075. The file CMakeLists.txt can be used to install these plugins as shared libraries
against your ASPECT installation with:

1. Enter plugins directory
2. cmake -DAspect_DIR=/path/to/ASPECT/installation/ .
3. make

## FastScape version

The FastScape source code provided in this repository corresponds to commit 592595752e11904e2350159ab0fd50fa37a843b6 
of the FastScape branch [https://github.com/anne-glerum/fastscapelib-fortran/tree/fastscape-with-stratigraphy-for-aspect](https://github.com/anne-glerum/fastscapelib-fortran/tree/fastscape-with-stratigraphy-for-aspect) 
and can be found in the folder /src_FastScape of Zenodo archive https://doi.org/10.5281/zenodo.10048075. This branch is built on commit 18f25888b16bf4cf23b00e79840bebed8b72d303 of 
[https://github.com/fastscape-lem/fastscapelib-fortran](https://github.com/fastscape-lem/fastscapelib-fortran).


## ASPECT input files
The ASPECT input files can be found in the folder /prms and their name corresponds to the folders with model outputs also in this repository.
The names include the following information::
5p - narrow asymmetric (NA) rift simulations
5q - narrow symmetric (NS) rift simulations
5o - wide (W) rift simulations
craton400000.0 - initial distance between rift and craton edge of 50 km (as rift centre lies at 350 km)
craton450000.0 - initial distance between rift and craton edge of 100 km (as rift centre lies at 350 km)
craton500000.0 - initial distance between rift and craton edge of 150 km (as rift centre lies at 350 km)
seed1236549 - first of nine initial plastic strain configurations
As an example, simulation NA-4-50km of Fig. 1 of the paper corresponds to folder 5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0.

## ASPECT output files
The folder belonging to each simulation includes ASPECT output files log.txt and statistics. The statistics files have been used to plot source rock area over time with the scripts provided in the main folder. Raw vtu files are also included for specific snapshots shown in the paper.

## FastScape output files
Raw vtu files are included for those snapshots that are shown in the paper in the respective folders of their simulations.

## FastScape installation details
The FastScape version in Zenodo archive https://doi.org/10.5281/zenodo.10048075 can by installed by:
1. Cloning this repository
2. Creating a build directory and entering it 
3. cmake -DBUILD_FASTSCAPELIB_SHARED=ON /path/to/fastscape/dir/
4. make

## ASPECT Installation details
ASPECT was built using the underlying library deal.II 10.0.0-pre (master, d944f3d291)
on the German HLRN cluster Lise. deal.II used:
* 32 bit indices and vectorization level 3 (512 bits)
* Trilinos 12.18.1
* p4est 2.2.0

The ASPECT version in Zenodo archive https://doi.org/10.5281/zenodo.10048075 can be installed by (assuming deal.II is installed):
1. Creating a build directory and entering it
2. cmake -DEAL_II_DIR=/path/to/dealii/dir/ -DFASTSCAPE_DIR=/path/to/fastscape/build/dir/ path/to/aspect/dir/
3. make

## Preprocessing
The folder /preprocessing_scripts contains python 3.9.17 scripts to generate and plot initial topography and lithospheric layer thicknesses for the craton that are in isostatic balance with the reference lithosphere. The resulting initial topography files are provided in the folder /prms

## Postprocessing
Images of model results were created with the ParaView 5.13.1 python scripts and statefiles in the folder /postprocessing_scripts (sedtype_fav_ore_form_8.py files and pvsm state files for ASPECT and FS.py for FastScape).
Plots of source rock area over time were created with python 3.9.17 scripts that can also be found in the /postprocessing_scripts folder.
To count the occurrences of source rock, host rock and their overlaps of faults, the following scripts were run:
1. identify_source_rock_in_image.py (count occurrences at every 0.5 My for each simulation)
2. identify_OS_and_write_new_stats_summary.py (update that takes into account the start of oceanic spreading)
3. create_stats_summary.py (summarize results of each simulation)
4. create_stats_summary_suite.py (summarize results of each suite of 9 simulations)
The different plots of the results in the Supplement are made with:
regime_diagram_dOFM.py
regime_diagram_dOFM_5o.py
regime_diagram_dcraton.py
regime_diagram_dcraton_5p.py
regime_diagram_nmax.py
regime_diagram_nmax_5p.py
Figure 9 was created with:
plot_traffic_light_5o_craton_distances_fixed_bothres.py
plot_traffic_light_5p_craton_distances_fixed_bothres.py
Note that only the base path will need to be adapted for the scripts to find the simulations.
