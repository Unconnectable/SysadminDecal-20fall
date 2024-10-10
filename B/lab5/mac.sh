#!/bin/bash

#使用以下来修正unix的换行问题
#sed -i 's/\r$//' mac.sh
#或者在安装了dos2unix之后 使用 dos2unix <filename>

mac_address=$(ip link show eth0 | awk '/link\/ether/ {print $2}')

if [ -n "$mac_address" ] ; then
	echo "MAC_ADDRESS IS $mac_address"
else
	echo "FAIL TO ACCESS MAC_ADDRESS"
fi