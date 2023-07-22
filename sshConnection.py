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

