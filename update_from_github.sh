#!/bin/bash
OUT=$(git -C /home/pi/programming/python/laststand/lastStandBot pull origin)
if [[ $OUT == "Already up to date." ]]; then
  echo "No changes. No restart"
else
  sudo systemctl restart laststandbot
fi