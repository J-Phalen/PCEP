# ### Task 1.3: Create print_system_info() function
# Use the platform module to display system information.

# **Requirements:**
# - Import the `platform` module
# - Print: `platform.system()`, `platform.python_version()`, `platform.machine()`
# - Format output nicely with labels

# **Example Output:**
# ```
# System: Windows
# Python Version: 3.11.0
# Machine: AMD64
# ```

# ---

import platform


def print_system_info():
    """Prints basic system information including OS, Python version, and machine type."""
    system = platform.system()
    pyVersion = platform.python_version()
    machine = platform.machine()

    return {"system": system, "pyVersion": pyVersion, "machine": machine}


SysInfo = print_system_info()

if SysInfo.get("system"):
    print(f"System: {SysInfo.get('system')}")
if SysInfo.get("pyVersion"):
    print(f"Python Version: {SysInfo.get('pyVersion')}")
if SysInfo.get("machine"):
    print(f"Machine: {SysInfo.get('machine')}")
