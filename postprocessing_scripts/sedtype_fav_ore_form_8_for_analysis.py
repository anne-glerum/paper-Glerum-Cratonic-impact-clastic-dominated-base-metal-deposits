# trace generated using paraview version 5.7.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
from os.path import exists

file_name_base = '/scratch/usr/bbpanneg/runs/FastScapeASPECT_cratons/'

# res_x default = 4000
res_x = 4000
# res_y default = 500
res_y = 500
# cam_parllel_scale default = 25000
cam_parallel_scale = 25000
# cam_y default = 280000
cam_y = 280000

model_names = [
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5p_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5o_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
##
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton450000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
#'5q_fixed_CERI_surfPnorm_htanriftcraton_inittopo_craton500000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
 ]

# Loop over all models
for m in model_names: 

  #ASPECT_time_steps = ['00000','00001','00002','00003','00004','00005','00006','00007','00008','00009','00010','00011','00012','00013','00014','00015','00016','00017','00018','00019','00020','00021','00022','00023','00024','00025','00026','00027','00028','00029','00030','00031','00032','00033','00034','00035','00036','00037','00038','00039','00040','00041','00042','00043','00044','00045','00046','00047','00048','00049','00050']
  #ASPECT_time_steps = ['00000','00001','00005','00010','00015','00020','00025','00030','00035','00040','00045','00050']
  #ASPECT_time_steps = ['00002','00003','00004','00006','00007','00008','00009','00011','00012','00013','00014','00016','00017','00018','00019','00021','00022','00023','00024','00026','00027','00028','00029','00031','00032','00033','00034','00036','00037','00038','00039','00041','00042','00043','00044','00046','00047','00048','00049']
  ASPECT_time_steps = ['00005']

  for t in range(0,len(ASPECT_time_steps)):
  
    print("Model name: ", m)
    print ("Time step number: ", ASPECT_time_steps[t])
  
    ASPECT_filename=file_name_base+m+'/solution/solution-'+ASPECT_time_steps[t]+'.pvtu'

    file_exists = exists(ASPECT_filename)
    if not file_exists:
      print ("File does not exist, continuing")
      continue
  
    # load state
    LoadState('/scratch/usr/bbpanneg/postprocessing/CERI_cratons/9_no1350isotherm_onlysource_host_strain_strainrate.pvsm',
        LoadStateDataFileOptions='Choose File Names',
        DataDirectory='/scratch/usr/bbpanneg/postprocessing/CERI_cratons/',
        solutionpvtuFileName=[ASPECT_filename])
    
    renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
    renderView1.ViewSize = [2560, 1920]
  
    # Hide sea level
    line2 = FindSource('Line2')
    Hide(line2, renderView1)

    # current camera placement for renderView1
    position = 350000. #centered zoom2
    renderView1.CameraPosition = [position, cam_y, 550000]
    renderView1.CameraFocalPoint = [position, cam_y, -43924.18361557276]
    renderView1.CameraViewUp = [0.0, 1., 0.]
    renderView1.CameraParallelScale = cam_parallel_scale
    
    renderView1.ViewSize = [res_x, res_y] 
    LoadPalette(paletteName='WhiteBackground')

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_source_host_strain_strainrate_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)
  
    # Turn off strain and strain rate 
    calculator_plasticstrain_z0 = FindSource('Calculator_plasticstrain_z0')
    clip_strainrate_z4 = FindSource('Clip_strainrate_z4')
    Hide(calculator_plasticstrain_z0, renderView1)
    Hide(clip_strainrate_z4, renderView1)

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_source_host_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)


    # Host only
    clip_Sand_250C_z15 = FindSource('Clip_Sand_>250C_z15')
    Hide(clip_Sand_250C_z15, renderView1)

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_host_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)

    # Source only
    clip_Sand_250C_z15Display = Show(clip_Sand_250C_z15)
    clip_silicates_150C_z10 = FindSource('Clip_silicates_<150C_z10')
    clip_limestones_150C_z10 = FindSource('Clip_limestones_<150C_z10')
    clip1_carbonates_150C_z10 = FindSource('Clip1_carbonates_<150C_z10')
    Hide(clip_silicates_150C_z10, renderView1)
    Hide(clip_limestones_150C_z10, renderView1)
    Hide(clip1_carbonates_150C_z10, renderView1)

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_source_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)

    # Only show strain rate
    clip_strainrate_z4Display = Show(clip_strainrate_z4, renderView1)
    Hide(clip_Sand_250C_z15, renderView1)

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_strainrate_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)

    # Only show plastic strain in greyscale
    Hide(clip_strainrate_z4, renderView1)
    # set active source
    SetActiveSource(calculator_plasticstrain_z0)
    calculator_plasticstrain_z0Display = Show(calculator_plasticstrain_z0, renderView1)

    # get color transfer function/color map for 'PlasticStrain'
    plasticStrainLUT = GetColorTransferFunction('PlasticStrain')
    
    # get opacity transfer function/opacity map for 'PlasticStrain'
    plasticStrainPWF = GetOpacityTransferFunction('PlasticStrain')
    
    # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
    plasticStrainLUT.ApplyPreset('X Ray', True)

    # save screenshot
    output_filename=file_name_base+m+'/'+m+'_'+ASPECT_time_steps[t]+'_plasticstrain_8_zoom2_'+ str(cam_y)+'_'+str(cam_parallel_scale)+'.png'
    SaveScreenshot(output_filename, renderView1, ImageResolution=[res_x, res_y],
        TransparentBackground=0)

    # Delete sources and their children
    for x in GetSources().values():
      Delete(x[0])
