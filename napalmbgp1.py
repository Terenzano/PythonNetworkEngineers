import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'cisco', 'cisco')
iosvl2.open()

bgp_neighbors = iosvl2.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

