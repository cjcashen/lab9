import os
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import NetMikoTimeoutException
from getpass import getpass

USERNAME = input("Pleae enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

ciscoDevice = {
    'host': '192.168.211.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

try:
    conncetion = ConnectHandler(**ciscoDevice)
except (NetMikoTimeoutException):
    print ('The following device timed out: ' + ciscoDevice['host'])

except (SSHException):
    print('Could not connect to the device with SSH. Check your SSH settings on: ' + ciscoDevice['host'])

except (AuthenticationException):
    print('Could not authenticate user on' + ciscoDevice['host'])
print("script successfully completed")
c = ConnectHandler(**ciscoDevice)

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)
f.close()
