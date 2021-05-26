# pihole_customdns
Pi-hole customDNS class

### Usage:
```
from pihole import pihole_api

pihole = pihole_api("http://pihole-ip:80", "password")
pihole.add_custom_dns("domain", "ip")
```
