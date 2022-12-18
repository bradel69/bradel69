#
# author:   Luis Bras
# date:     2022.09.13
# objetive: how to verify if router external ip has changed, is so notify by email
#
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
# get external ip
EXTERNAL_ATUAL_IP=$(curl -s http://whatismyip.akamai.com/)
# verify last ip
OLD_IP=$(cat /root/scripts/old_ip.txt)
# create file to send by email
# write date
date > /root/scripts/email_external_ip.txt
# write external ip
echo "External IP address: $EXTERNAL_ATUAL_IP" >> /root/scripts/email_external_ip.txt
# write old external ip
echo "Old IP address: $OLD_IP" >> /root/scripts/email_external_ip.txt
if [ "$EXTERNAL_ATUAL_IP" = "$OLD_IP" ]; then
  echo "ok"
else
  # if diferent send email
  mpack -s "external ip changed" /root/scripts/email_external_ip.txt email@server.com
  echo "$EXTERNAL_ATUAL_IP" > /root/scripts/old_ip.txt
fi
