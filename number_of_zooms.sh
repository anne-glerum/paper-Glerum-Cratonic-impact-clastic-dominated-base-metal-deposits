#!/bin/bash

while read name;
do
  echo $name
  if [ ! -d "$name" ]; then
    continue
  fi
  ls $name"/"$name*"sedage2_8_zoom2"*".png" | wc -l
done < list_of_model_names.txt

