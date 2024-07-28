import os
import platform
import json
import Data
import time

def FPS_lock(FPS = 60):
    act_time = time.time()
    d_time = 0
    while d_time < (1/FPS):
        d_time = time.time()-act_time
        time.sleep(0.001)
    return 0

def write_sys_inf():
    with open('Data/OS.txt', 'w') as fuck:
        fuck.write(f'{platform.system()}\n{platform.platform()}')

def write_settings_def():
    with open('Data/settings.js', 'w') as fuck:
        fuck.write(json.dumps(Data.defa_settings, indent=2))

def show_os():
    with open('Data/OS.txt', 'r') as fuck:
        fuck.readline()
        return fuck.readline()

def clear_window():
    with open('Data/OS.txt', 'r') as fuck:
        a = str(fuck.readline().strip())
        match a:
            case 'Windows':
                os.system('cls')
            case 'Linux':
                os.system('clear')
            case 'unknown':
                os.system('cls||clear')
            case _:
                print('error')
