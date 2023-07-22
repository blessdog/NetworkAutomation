# NetworkAutomation
Scripts for automating networking tasks
Automating a network task using Python generally involves using libraries such as netmiko, paramiko for SSH connections or requests for HTTP requests. You can automate tasks such as configuration changes, information retrieval (like interface status, CPU usage, etc.), and many more.

Here is an example of a simple network automation task: retrieving the configuration of a network device using netmiko:
from netmiko import ConnectHandler
```python
def get_device_config(ip, username, password, device_type):
    device = {
        'device_type': device_type,
        'ip':   ip,
        'username': username,
        'password': password,
    }

    connection = ConnectHandler(**device)

    print("Connected to the device!")

    output = connection.send_command('show running-config')
    connection.disconnect()

    return output

config = get_device_config('10.0.0.1', 'admin', 'password', 'cisco_ios')
print(config)
```
This script will connect to a Cisco device at IP address '10.0.0.1' using the username 'admin' and password 'password', run the command show running-config, and then disconnect. The show running-config command is a common command on Cisco devices that shows the current configuration of the device.

Note: Replace '10.0.0.1', 'admin', 'password', and 'cisco_ios' with the actual IP address, username, password, and device type of the device you are connecting to.

This is just a basic example. Network automation can get quite complex, depending on the tasks you're looking to perform. But Python, with its extensive libraries and easy syntax, is a great tool for network automation tasks.

Please make sure you have the necessary permissions before attempting to connect or make changes to any network device. Misuse could lead to serious network issues.

---

Here is another example, this time using the library paramiko for a simple SSH connection to retrieve system information:
```python
import paramiko

def get_system_info(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh.connect(hostname, port, username, password)

    stdin, stdout, stderr = ssh.exec_command('uname -a')
    system_info = stdout.read().decode()
    
    ssh.close()

    return system_info

info = get_system_info('your_host', 22, 'your_username', 'your_password')
print(info)
```
This script connects to a remote system using SSH, executes the command uname -a which is a common Unix command to fetch system information, then disconnects. The system information is returned as a string.

Please replace 'your_host', '22', 'your_username', and 'your_password' with the actual hostname/IP, port number, username, and password of the system you want to connect to.

Remember to handle exceptions for error handling. This example assumes ideal conditions for simplicity. In a production-level script, you would want to manage SSH failures, command failures, and other exceptions.

Also, as always, ensure you have the necessary permissions before running any command on a remote system

