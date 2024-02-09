#!/bin/bash

while read name;
do
  echo $name
  if [ ! -d "$name" ]; then
    mkdir $name
  fi
  if [ ! -d "$name/VTK" ]; then
    mkdir $name"/VTK"
  fi

  # get snapshots at 1, 2, 3, 4, 5, 10, 15, 20, 25 My
  cp "/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"$name"/VTK/Topography000"{0289,0575,0861,1147,1432,2861,4289,5718,7147}".vtk" $name"/VTK/"

done < list_of_model_names.txt

