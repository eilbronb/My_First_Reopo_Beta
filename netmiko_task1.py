from netmiko import ConnectHandler

cisco_gns3 = {'device_type':'cisco_ios',
              'ip':'10.10.10.30',
              'username':'admin',
              'password':'admin'}

connection = ConnectHandler(**cisco_gns3)

hostname = connection.find_prompt()
print(hostname[:-1])

interface_name = connection.send_command('show run int eth0/0 | i ^ interface')
print(interface_name)

interface_description = connection.send_command('show run int eth0/0 | i ^ des')
if not interface_description:
    interface_description = 'N/A'
print(interface_description)

Config1 =['interface loopback0', 'ip address 100.100.100.100 255.255.255.255']

connection.config_mode()
create_loopback = connection.send_config_set(Config1)
print(create_loopback)

verification = connection.send_command('show ip interface brief | include Loopback')
if verification.count('up') == 2:
    print('It looks like Loopback0 is "up/up"! Way to go!')
else:
    print('It looks like something went wrong, let\'s get out before we break something!')
print(verification)

print('Moving on to Eth0/0, Eth0/1, Eth0/2 ')
Config2 =['interface eth0/1','switchport',
         'des To R1', 'switchport mode access' 'switchport access vlan 10',
         'no shut', 'interface eth0/0','switchport',
         'des To IOU-L3', 'switchport mode access' 'switchport access vlan 10',
         'no shut', 'interface eth0/2','switchport',
         'des To IOU2', 'switchport mode access' 'switchport access vlan 10',
         'exit']
connection.send_config_set(Config2)

output0 = connection.send_command('show ip int eth0/1 | i Ethernet0/1')
if output0.count('up') == 2:
    print('It Looks like Ethernet0/1 is "up/up", Way to go!')
else:
    print('It looks like Something went wrong, let\'s exit before we break something')
    sys.exit()
output1 = connection.send_command('show ip int eth0/0 | i Ethernet0/0')
if output0.count('up') == 2:
    print('It Looks like Ethernet0/0 is "up/up", Way to go!')
else:
    print('It looks like Something went wrong, let\'s exit before we break something')
    sys.exit()
output2 = connection.send_command('show ip int eth0/2 | i Ethernet0/2')
if output0.count('up') == 2:
    print('It Looks like Ethernet0/2 is "up/up", Way to go!')
else:
    print('It looks like Something went wrong, let\'s exit before we break something')
    sys.exit()
