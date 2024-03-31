import webbrowser
import urllib.parse
import sys
import datetime
import os
import platform
import subprocess
from colorama import *

### initialisation ###

init()

### DEFS ###
def search_google(query):
    encoded_text = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={encoded_text}"
    webbrowser.open(search_url)
    print(f'<google_search> Searching "{query}" on Google...')

def open_url(url):
    encoded_text = urllib.parse.quote(url)
    search_url = f"https://{encoded_text}"
    webbrowser.open(search_url)
    print(f'<url_con> Opening URL: "{url}"')

def see_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
    print("Тime now:", formatted_time)

def clear_console():
    os.system('cls')

def shutdown_pc():
    os.system("shutdown /s /t 0")

def reboot_pc():
    os.system("shutdown /r /t 0")

def sleep_pc():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def get_isystem():

    os_name = platform.system()
    os_version = platform.version()
    architecture_inf = platform.machine()
    cpu_info = subprocess.check_output('wmic cpu get name', shell=True).decode('utf-8').strip()

    
    try:
        import wmi
        w = wmi.WMI()
        video_controller = w.Win32_VideoController()[0].Caption
    except ImportError:
        video_controller = "N/A"

    try:
        import wmi
        w = wmi.WMI()
        motherboard = w.Win32_BaseBoard()[0].Product
    except ImportError:
        motherboard = "N/A"

    current_user = os.getlogin()

    list_isys = ["OS: " + os_name, "OS ver: " + os_version, "Architecture: " + architecture_inf, "CPU: " + cpu_info, "Display adapter: " + video_controller, "MB: " + motherboard]
    print("System Information:")
    
    for item in list_isys:
        print(item)

    if video_controller == "N/A" or motherboard == "N/A":
        print(Fore.RED + "\nSome elements are displayed incorrectly, you may be missing some libraries.\nUse get_drive to download them." + Style.RESET_ALL)
def restart_script():
    print("The program will be restarted..")
    script = sys.argv[0] 
    subprocess.call([sys.executable, script] + sys.argv[1:])

def open_file_explorer():
    try:
        subprocess.Popen('explorer', shell=True)
    except Exception as e:
        print(f"Error to opened: {e}")
     
### DOWNLOADER LIBARY ###
def install_library():
    try:
        subprocess.check_call(['pip', 'install', 'wmi'])
        print("The 'wmi' library has been successfully installed.")
    except Exception as e:
        print("An error occurred while installing the 'wmi' library:", str(e))

    try:
        subprocess.check_call(['pip', 'install', 'colorama'])
        print("The 'colorama' library has been successfully installed.")
        restart_script()
    except Exception as e:
        print("An error occurred while installing the 'wmi' library:", str(e))

    

### MAIN ###
def main():
    print("Windows Set Utility >> 0.3.1 SYS")
    while True:
        user_cmd = input("WS >> ").strip()
        cmd = user_cmd.split()

        if "serfg" in cmd:
            serfg_index = cmd.index("serfg")
            search_text = " ".join(cmd[serfg_index + 1:])
            search_google(search_text)

        elif "serf" in cmd:
            serf_index = cmd.index("serf")
            url_text = " ".join(cmd[serf_index + 1:])
            open_url(url_text)

        elif "time" in cmd:
            see_time()

        elif "clear" in cmd or "cl" in cmd:
            clear_console()

        elif "shutdown" in cmd:
            print('Turning off..')
            shutdown_pc()

        elif "reboot" in cmd:
            print('Rebooting..')
            reboot_pc()

        elif "sleep" in cmd:
            print('Switching to sleep..')
            sleep_pc()

        elif "isys" in cmd:
            print("Getting information..")
            get_isystem()

        elif "opf" in cmd:
            open_file_explorer()

        ### SPECIAL ###
        elif "help" in cmd:
            help_text = """
            Cm with program:
            end
            restart
            get_drive
            clear

            Cm with Internet:
            serf <url>
            serfg <text>

            Cm with files:
            opf
            
            Cm with system:
            time
            isys
            shutdown
            reboot
            sleep
            """
            print(help_text)

        elif "get_drive" in cmd:
            print("Downloading required libraries..")
            install_library()

        elif "end" in cmd:
            sys.exit()

        elif "restart" in cmd:
            restart_script()

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()