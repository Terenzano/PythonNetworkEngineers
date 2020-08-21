import json
from napalm import get_network_driver

devicelist = ['192.168.122.72',
              '192.168.122.82',
              '192.168.122.83',
              '192.168.122.84'
             ]

for ip_address in devicelist:
    print('Connecting to ' + str(ip_address))
    driver = get_network_driver('ios')
    iosvl2 = driver(ip_address, 'cisco', 'cisco')
    iosvl2.open()
    iosvl2.load_merge_candidate(filename='ACL1.cfg')
    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No ACL changes required')
        iosvl2.discard_config()

    iosvl2.load_merge_candidate(filename='OSPF.cfg')
    diffs = iosvl2.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosvl2.commit_config()
    else:
        print('No OSPF changes required')
        iosvl2.discard_config()

iosvl2.close()

