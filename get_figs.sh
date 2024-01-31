#!/bin/bash

while read name;
do
  echo $name
  if [ ! -d "$name" ]; then
    mkdir $name
  fi
  cp "/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"$name"/"$name*"sedage2_8_zoom2"*".png" $name"/"
  cp "/Users/acglerum/Documents/Postdoc/SB_CRYSTALS/HLRN/HLRN/FastScapeASPECT_cratons/"$name"/"$name*"sedage2_8_wholedomain"*".png" $name"/"
done < list_of_model_names.txt

