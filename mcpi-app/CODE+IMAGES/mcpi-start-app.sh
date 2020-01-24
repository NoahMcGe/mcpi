#!/bin/sh
cd ~/Desktop/mcpi-app/

if grep -q okay /proc/device-tree/soc/v3d@7ec00000/status; then
	export LD_PRELOAD=libbcm_host.so.1.0
	export LD_LIBRARY_PATH=lib/mesa
else
	export LD_LIBRARY_PATH=lib/brcm
fi

./minecraft-pi
