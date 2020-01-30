#!/bin/bash

if [[ -z "$1" || -z "$2" ]]; then 
   echo "Usage:
sudo $0 <your PizzaMining account username> <this unique rig name>"
   exit
fi

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root:
sudo $0 $1" 
   exit
fi

echo "$1" > /mine/username
echo "$2" > /mine/rig

RED='\033[4;3;1;31m'
END='\033[0m'

echo -e "${RED}Welcome to \033[5;31mPIZZA MINING!!!${END}
Installing..."

mkdir -p /mine/
mkdir -p /mine/miners/
wget "https://raw.githubusercontent.com/JonPizza/PizzaMiningClient/master/main.py" -q -P /mine/
wget "https://raw.githubusercontent.com/JonPizza/PizzaMiningClient/master/trex.py" -q -P /mine/
wget "https://raw.githubusercontent.com/JonPizza/PizzaMiningClient/master/install_miner.sh" -q -P /mine/miners/
echo "@reboot python3 /mine/main.py" | crontab -

echo "Installed PizzaMining Software. 
Installing Nvidia Drivers (this may take a while)..."

apt-get install nvidia-driver-390 -y > /dev/null
apt-get install nvidia-driver-435 -y > /dev/null

echo -e "${RED}Installed Successfully. After reboot mining will begin.${END}"
echo "Reboot in 5"
sleep 1
echo "4"
sleep 1
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1

reboot
