# This file is creating for saving config.json file by time for training every time.
# save dir: /details

import time
from shutil import copyfile

t = time.localtime()
name_str = str(t.tm_year) + '-' + str(t.tm_mon) + '-' + str(t.tm_mday) + '-' + str(t.tm_hour) + '-' + str(t.tm_min) + '-' + str(t.tm_sec)
copyfile('config.json', './details/config-' + name_str + '.json')

print(name_str)