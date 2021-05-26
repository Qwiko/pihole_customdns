from requests import Session
import logging

'''
Class for Pi-hole customdns
Usage:
from pihole import pihole_api

pihole = pihole_api("http://pihole-ip:80", "password")
pihole.add_custom_dns("domain", "ip")
'''

class pihole_api():
    def __init__(self, url, pw="", verify_ssl=True, logger=None):
        self.log = logger if logger else logging.getLogger(__name__)
        self._base_url = f"{url}/admin"
        self._customdns_url = self._base_url + "/scripts/pi-hole/php/customdns.php"
        self._verify_ssl = verify_ssl
        self._session = Session()
        self.login(pw)
        
    def _send(self, data={}, action="get"):
        data["action"] = action
        data["token"] = self._token
        r = self._session.post(self._customdns_url, data=data, verify=self._verify_ssl)
        return r.json()

    def login(self, pw):
        r = self._session.post(self._base_url + "/index.php?login", data={"pw": pw}, verify=self._verify_ssl)
        self.set_token(r)

    def extract_token(self, r):
        for row in r.text.split("\n"):
            if "token" in row and "hidden" in row:
                token = row.split(">")[-2].split("<")[0]
                return token

    def set_token(self, r):
        token = self.extract_token(r)
        if not token:
            self.log.error("TOKEN NOT FOUND, LOGIN ERROR, EXITING!")
            exit(1)
        self._token = token

    def get_custom_dns(self):
        r = self._send()
        return r
    
    def del_custom_dns(self, domain, ip):
        data = {
            "domain": domain,
            "ip": ip
        }
        r = self._send(data, "delete")
        return r

    def add_custom_dns(self, domain, ip):
        data = {
            "domain": domain,
            "ip": ip
        }
        r = self._send(data, "add")
        return r