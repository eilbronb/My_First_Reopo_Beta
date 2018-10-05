from netmiko import ConnectHandler

cisco_gns3 = {'device_type':'cisco_ios',
              'ip':'10.10.10.30',
              'username':'admin',
              'password':'admin'}

connection = ConnectHandler(**cisco_gns3)

hostname = connection.find_prompt()
print(hostname)
