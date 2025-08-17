import schedule
import time 
import subprocess
import sys
import random
import datetime

def bing_reward():
    subprocess.Popen(['python', ''])

#runs a script
def run_script(path):
    if path.endswith(".py"):
        subprocess.Popen([sys.executable, path], shell=True)
    else:
        subprocess.Popen(path, shell=True)

#returns a random time in format of 12:34
def random_hour(start_hour = 0, end_hour=23):
    hour = random.randint(start_hour, end_hour)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"