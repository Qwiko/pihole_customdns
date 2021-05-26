# pihole_customdns
PiHole CustomDNS class in Python3

### Usage:
```
from pihole import pihole_api

pihole = pihole_api("http://pihole-ip:80", "password")
pihole.add_custom_dns("domain", "ip")
```
