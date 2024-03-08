from PIL import Image
from PIL import ImageDraw as ID
from PIL import ImageOps as IO
from PIL import ImageFont
from os.path import exists

# model name
model_name_tails = [
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed1236549_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed2323432_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed2349871_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed2928465_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed3458045_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed5346276_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed7646354_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed9023857_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
'5p_fixed_CERI_surfPnorm_craton400000.0_A0.25_seed9872345_rain0.0001_Ksilt210_Ksand70_Kf1e-05_SL-200_vel10_tmax25000000.0',
                   ] 
                    
# timesteps [My]
timesteps = ['01', '05', '15', '25', '35', '45', '55', '65', '75', '85', '95']

# the scaling factor for each individual image
scale = 0.75
# the scaling factor for the space between images
empty = 0.025
# the original dimension of each image
x_orig = 4000
y_orig = 500
# the relative size of the border
border = int(2*empty*scale*x_orig)
# font size
font_size = 70

# start with an empty figure of the right size
n_x = 1
n_y = 11
# set font
font_test = ImageFont.truetype("/System/Library/Fonts/Supplemental/arial.ttf",font_size)


for m in model_name_tails:

  print (m)
  total = Image.new("RGB", (int(2*border+n_x*scale*x_orig+(n_x-1)*empty*scale*x_orig),int(2*border+n_y*scale*y_orig+(n_y-1)*empty*scale*x_orig)))
  # object for text and shapes
  draw = ID.Draw(total)

  for i,t in enumerate(timesteps):

    try:
      # load the figure
      img = Image.open(m+"/"+m+"_000"+t+"_heatfluxcontours_sedtypes_Tcontours_source_host_sedage2_8_zoom2_280000_25000.png")
      # arrange the figure
      total.paste(IO.scale(img,scale), (int(border+(n_x-1)*scale*x_orig+(n_x-1)*empty*scale*x_orig),int(border+i*scale*y_orig+i*empty*scale*x_orig)))
  
    except FileNotFoundError:
      pass
  
    # write the timestep
    draw.text((int(border+(n_x-1)*scale*x_orig+(n_x-1)*empty*scale*x_orig),int(border+(i)*scale*y_orig+(i)*empty*scale*x_orig)),t,font=font_test,anchor="ld")
  
  # write the model name
  draw.text((int(border+(n_x-1)*scale*x_orig+(n_x-1)*empty*scale*x_orig),int(border+scale*y_orig)),m,font=font_test,anchor="ld",fill="black")

  # draw ellipses around co-occurrences
  m_c1 = 27
  n_c1 = 6.
  x_c1 = 0.65
  y_c1 = 0.15
  x0_c1 = border+(m_c1-1.)*empty*scale*x_orig+scale*x_orig*(m_c1-1.+x_c1)
  y0_c1 = border+(n_c1-1.)*empty*scale*x_orig+scale*y_orig*(n_c1-1.+y_c1)

  # save
  total.save(m + "/" + m + "_allt_sedage2_zooms.png")
  # to avoid keeping figures from the previous simulation, close
  total.close()
