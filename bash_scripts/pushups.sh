#!/bin/bash
x=1

while [[ $x -le 100 ]]
do

##  echo " Hey i just did $x pushups"

read -p " Pushup $x : Press enter to continue"
  ((x ++))
done

echo " Congrads , you completed your pushups !!"
