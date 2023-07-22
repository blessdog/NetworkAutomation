from netmiko import ConnectHandler

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

