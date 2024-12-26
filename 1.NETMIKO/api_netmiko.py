#! /usr/bin/env python
"""
Learning Series: Network Programmability Basics
Module: Programming Fundamentals
Lesson: Python Part 3
Author: Hank Preston <hapresto@cisco.com>

api_netmiko_example.py
Illustrate the following concepts:
- Making CLI calls using netmiko library
- Intended to be entered into an interactive
  interpreter
"""

from netmiko import ConnectHandler
import os

# Define device details
ios_xe_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
    'secret': 'enable_password',
}

# Function to connect and send show command
def send_show_command(device, command):
    with ConnectHandler(**device) as conn:
        conn.enable()
        output = conn.send_command(command)
        return output

# Function to send configuration commands
def send_config_commands(device, commands):
    with ConnectHandler(**device) as conn:
        conn.enable()
        output = conn.send_config_set(commands)
        return output

# Function to backup device configuration
def backup_configuration(device, backup_file):
    show_run = send_show_command(device, 'show running-config')
    with open(backup_file, 'w') as file:
        file.write(show_run)

# Function to send configuration using an external file
def send_config_from_file(device, config_file):
    with open(config_file, 'r') as file:
        commands = file.read().splitlines()
    return send_config_commands(device, commands)

# Function to configure a subset of interfaces
def configure_interfaces(device, interface_configs):
    commands = []
    for interface, config in interface_configs.items():
        commands.append(f"interface {interface}")
        commands.extend(config)
        commands.append("exit")
    return send_config_commands(device, commands)

# Function to connect to multiple devices

def send_commands_to_multiple_devices(devices, command, config=False):
    results = {}
    for device in devices:
        if config:
            results[device['host']] = send_config_commands(device, command)
        else:
            results[device['host']] = send_show_command(device, command)
    return results

# Example use cases
if __name__ == "__main__":
    # Send show commands to a single device
    show_output = send_show_command(ios_xe_device, 'show ip interface brief')
    print("Show Command Output:")
    print(show_output)

    # Send configuration commands to a single device
    config_commands = ['hostname IOS-XE-Router', 'no ip domain-lookup']
    config_output = send_config_commands(ios_xe_device, config_commands)
    print("Configuration Output:")
    print(config_output)

    # Backup device configuration
    backup_file_path = 'backup_config.txt'
    backup_configuration(ios_xe_device, backup_file_path)
    print(f"Configuration backed up to {backup_file_path}")

    # Send device configuration using an external file
    external_config_file = 'config_commands.txt'  # Ensure this file exists
    if os.path.exists(external_config_file):
        file_config_output = send_config_from_file(ios_xe_device, external_config_file)
        print("Configuration from file Output:")
        print(file_config_output)
    else:
        print(f"Config file {external_config_file} does not exist.")

    # Configure a subset of interfaces
    interface_configurations = {
        'GigabitEthernet0/0': ['description Uplink Interface', 'ip address 192.168.1.1 255.255.255.0', 'no shutdown'],
        'GigabitEthernet0/1': ['description Internal Interface', 'ip address 10.0.0.1 255.255.255.0', 'no shutdown']
    }
    interface_output = configure_interfaces(ios_xe_device, interface_configurations)
    print("Interface Configuration Output:")
    print(interface_output)

    # Send commands to multiple devices
    devices = [
        ios_xe_device,  # Add more device dictionaries as needed
    ]
    multiple_device_output = send_commands_to_multiple_devices(devices, 'show version')
    print("Output from Multiple Devices:")
    for device, output in multiple_device_output.items():
        print(f"Device {device}:")
        print(output)
