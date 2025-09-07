#!/bin/bash
set -e

#Init DB if not exists
#echo "Checking if database needs initialization..."
#export PGPASSWORD=$DBROOTPW
#kamdbctl create || true

# Start Kamailio
#exec kamailio -DD -E -f /etc/kamailio/kamailio.cfg

echo "Starting Kamailio with Python KEMI..."
exec kamailio -DD -E -e
