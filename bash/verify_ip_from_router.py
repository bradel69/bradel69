#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
EXTERNAL_ATUAL_IP=$(python3 /root/scripts/get_ip_from_router.py)
OLD_IP=$(cat /root/scripts/old_ip.txt)
date > /root/scripts/email_external_ip.txt
echo "External IP address: $EXTERNAL_ATUAL_IP" >> /root/scripts/email_external_ip.txt
echo "Old IP address: $OLD_IP" >> /root/scripts/email_external_ip.txt
if [ "$EXTERNAL_ATUAL_IP" = "$OLD_IP" ]; then
  echo "ok"
else
  mpack -s "external ip changed" /root/scripts/email_external_ip.txt lfdbras@gmail.com
  echo "$EXTERNAL_ATUAL_IP" > /root/scripts/old_ip.txt
fi
