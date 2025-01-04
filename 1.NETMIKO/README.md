# Part 3: Python Network automation with NETMIKO 


## Overview
This script demonstrates basic network programmability using the `netmiko` library in Python. It covers various operations for interacting with Cisco devices through CLI commands, including retrieving information, sending configurations, and automating repetitive tasks.

---

## Key Features

### 1. **Device Connection and CLI Interaction**
- Establishes a connection to a Cisco device using `netmiko.ConnectHandler`.
- Sends CLI commands to retrieve or modify the device configuration.

### 2. **Functions**
#### - `send_show_command(device, command)`
  - Sends a single show command to the device and returns the output.
  
#### - `send_config_commands(device, commands)`
  - Sends a list of configuration commands to the device and applies them.

#### - `backup_configuration(device, backup_file)`
  - Retrieves the running configuration of the device and saves it to a specified file.

#### - `send_config_from_file(device, config_file)`
  - Reads configuration commands from an external file and sends them to the device.

#### - `configure_interfaces(device, interface_configs)`
  - Configures specific interfaces with a given set of commands.

#### - `send_commands_to_multiple_devices(devices, command, config=False)`
  - Sends commands (show or config) to multiple devices and aggregates results.

### 3. **Example Use Cases**
- **Send Show Commands:** Retrieves and prints the output of `show ip interface brief`.
- **Apply Configurations:** Applies configuration changes such as setting a hostname and disabling domain lookup.
- **Backup Configurations:** Backs up the running configuration to a file.
- **Apply Configurations from File:** Reads and applies configurations from an external file.
- **Configure Interfaces:** Automates configuration of specific interfaces (e.g., IP address, description, enabling interfaces).
- **Multi-Device Management:** Sends commands to multiple devices and retrieves their outputs.

---

## Requirements
- Python 3.x
- `netmiko` library
- A Cisco IOS-XE device accessible over the network
- Proper credentials for device access

---

## Example Device Configuration
The script uses a dictionary for device details:
```python
ios_xe_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
    'secret': 'enable_password',
}
```

## Troubleshooting

It was a hassle to make this work in a dual router setup, but i eventually got it to work. 



