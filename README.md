# pihole_customdns
Pi-hole customDNS class

## Usage:
```
from pihole import pihole_api

pihole = pihole_api("http://pihole-ip:80", "password")
pihole.add_custom_dns("domain", "ip")
```

## Functions

### pihole.get_custom_dns()
Outputs a json object like the following:
```json
{ data:
    [
        ["host1.mgmt", "10.0.0.2"],
        ["host2.mgmt", "10.0.0.2"]
    ]
}
```

### pihole.del_custom_dns("host1.mgmt", "10.0.0.2")
Delete a domain entry. Output on success:
```json
{success: true, message: ""}
```

### pihole.add_custom_dns("host1.mgmt", "10.0.0.2")
Add a domain entry. Output on success:
```json
{success: true, message: ""}
```