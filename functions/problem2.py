"""
Problem: Write a function that accepts system name and any number of keyword arguments.
Return a formatted string showing the system name and its configuration details.
Use **kwargs.

def summarize_config(system_name, **config):
    pass

Expected Output:

# Expected Outputs for summarize_config()

# Test Case 1
# summarize_config("ArcusNode1", CPU="Intel", RAM="64GB")
# Output:
# System: ArcusNode1
# CPU: Intel
# RAM: 64GB

# Test Case 2
# summarize_config("SwitchAlpha", Ports=48, Type="Managed", Speed="1Gbps")
# Output:
# System: SwitchAlpha
# Ports: 48
# Type: Managed
# Speed: 1Gbps

# Test Case 3
# summarize_config("VM-01", OS="Ubuntu 22.04", vCPU=4, Memory="16GB", Disk="200GB")
# Output:
# System: VM-01
# OS: Ubuntu 22.04
# vCPU: 4
# Memory: 16GB
# Disk: 200GB

# Test Case 4
# summarize_config("StorageNodeX", Model="HPE 9300", Drives=24, Enclosure="2U")
# Output:
# System: StorageNodeX
# Model: HPE 9300
# Drives: 24
# Enclosure: 2U


"""

def summarize_config(system_name, **kwargs):
    print(f"System: {system_name}")
    for k,v in kwargs.items():
        print(f"{k}: {v}")
    print()

summarize_config("ArcusNode1", CPU="Intel", RAM="64GB")
summarize_config("SwitchAlpha", Ports=48, Type="Managed", Speed="1Gbps")
summarize_config("VM-01", OS="Ubuntu 22.04", vCPU=4, Memory="16GB", Disk="200GB")
summarize_config("StorageNodeX", Model="HPE 9300", Drives=24, Enclosure="2U")