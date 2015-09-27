# blocklist-update

/etc/dnsmasq/

  Contains block list, last version of block list and header file

/usr/local/bin/blocklist-update
  Script

/usr/lib/systemd/system/blocklist-update.service
  systemd service file - runs script

/usr/lib/systemd/system/blocklist-update.timer
  systemd timer file - runs blocklist-update.service once and hour
