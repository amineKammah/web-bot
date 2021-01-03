#!/bin/bash
sudo poff -a

while :
do
  while IFS= read -u 3 -r vpn && read -u 4 -r account
  do
    echo "Connecting to IP: $vpn, using $account"
    sub_pattern="s/#IP#/$vpn/"
    sed "$sub_pattern" pptp > /tmp/PPTP
    sudo cp /tmp/PPTP /etc/ppp/peers/PPTP
    sudo chmod 600 /etc/ppp/peers/PPTP
    sudo pon PPTP

    sleep 3

    python3 main.py $account

    sudo poff -a
  done 3<vpns 4<accounts
done