import os
import glob
import time
from threading import Thread
import random


# This file will look a little weird, but the key points are:
# - It's a little slow to read from the sensor, so we do that in a separate
# thread and store it in a global variable so as to not let the video stutter.
# - we use _running to prevent multiple copies of the file from being opened,
# which would waste resources but frankly also just because it makes ctrl-c
# work less well.

temp_fallback = 0

try:
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    temperature_file = device_folder + '/temperature'
except:
    temp_fallback = 999


_last_valid_temp = None
_running = False

# Public
def read_temp():
    if temp_fallback:
        return temp_fallback
    return _last_valid_temp


def read_ph():
    return random.uniform(6.8, 6.9)


def service():
    global _running
    if temp_fallback:
        return

    if not _running:
        _running = True
        Thread(target=_subprocess_get_temp).start()


# Private
def _subprocess_get_temp():
    global _last_valid_temp

    with open(temperature_file, 'r') as f:
        line = f.readline()
        _last_valid_temp = float(line) / 1000 # return celcius

    global _running
    _running = False
