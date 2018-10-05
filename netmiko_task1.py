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
print(verification)
