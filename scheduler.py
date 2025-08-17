import schedule
import time 
import subprocess
import sys
import random
import datetime

#runs a script
def run_script(path):
    if path.endswith(".py"):
        subprocess.Popen([sys.executable, path], shell=True)
    else:
        subprocess.Popen(path, shell=True)

#returns a random time in format of 12:34
def random_time(start_hour = 0, end_hour=23):
    hour = random.randint(start_hour, end_hour)
    minute = random.randint(0, 59)
    return f"{hour:02d}:{minute:02d}"

#coin flip
def boo():
    pot = [True, False]
    return random.choice(pot)

#random week
def schedule_random_week(path, times_per_week=3, start_hour=9, end_hour=17):
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    chosen_days = random.sample(days, times_per_week)  # pick random days
    for day in chosen_days:
        t = random_time(start_hour, end_hour)
        getattr(schedule.every(), day).at(t).do(run_script, path)
        print(f"Scheduled {path} on {day} at {t}")

#------------------Scripts After Here-------------------#

schedule_random_week(r"path-to-script", times_per_week=2, start_hour=9, end_hour=17)
schedule_random_week(r"path-to-script", times_per_week=3, start_hour=18, end_hour=23)
schedule_random_week(r"path-to-script", times_per_week=2, start_hour=1, end_hour=20)
schedule_random_week(r"path-to-script", times_per_week=3, start_hour=4, end_hour=8)

while True:
    schedule.run_pending()
    time.sleep(60)