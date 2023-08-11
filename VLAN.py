# High level script to create a VLAN using the 'ip' command in python.

import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Error executing command: {command}\n{error.decode()}")
        return None
    
    return output.decode()

def setup_vlan(nic, vlan_id, vlan_address):
    # Add the VLAN
    run_command(f"ip link add link {nic} name {nic}.{vlan_id} type vlan id {vlan_id}")

    # Bring the VLAN interface up
    run_command(f"ip link set {nic}.{vlan_id} up")

    # Assign IP Address to VLAN
    run_command(f"ip addr add {vlan_address} dev {nic}.{vlan_id}")

if __name__ == "__main__":
    # NIC name, for example 'eth0'
    nic_name = "eth0"

    # VLAN ID, a number between 1 and 4095
    vlan_identifier = 10

    # VLAN IP address and subnet, for example '192.168.10.1/24'
    vlan_ip_address = "192.168.10.1/24"

    setup_vlan(nic_name, vlan_identifier, vlan_ip_address)
    print(f"VLAN {vlan_identifier} set up on {nic_name} with IP address {vlan_ip_address}")

