import os
import subprocess
import importlib

try:
    subprocess.check_call(['pip', 'install', 'requests'])
    print("The 'requests' library has been successfully installed.")
except Exception as e:
    print("An error occurred while installing the 'requests' library:", str(e))

try:
    subprocess.check_call(['pip', 'install', 'wmi'])
    print("The 'wmi' library has been successfully installed.")
except Exception as e:
    print("An error occurred while installing the 'wmi' library:", str(e))

try:
    subprocess.check_call(['pip', 'install', 'colorama'])
    print("The 'colorama' library has been successfully installed.")
except Exception as e:
    print("An error occurred while installing the 'wmi' library:", str(e))
