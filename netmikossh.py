from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
<<<<<<< HEAD
    'ip': '192.168.122.72',
    'username': 'cisco',
    'password': 'cisco',
=======
    'ip' : '192.168.122.72',
    'username' : 'cisco',
    'password' : 'cisco',
>>>>>>> 4c09898df1e4474fcfb134d582b4f1cdf47050ea
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0' , 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,21):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output)

