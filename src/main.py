##!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages
import socket
import time
import sys
import threading
from datetime import datetime

#Threads
from ThreadTimer import ThreadTimer

#Libraries
import Settings

#Load files
SETTING_FILE = "settings.ini"

#Setting Val
Interval = 3

def task():
    print("Task---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S")))
    thread = threading.Timer(Interval, task)
    thread.start()

def main():
    settings = Settings.Settings(SETTING_FILE)
    interval = settings.load_settings()
    
    threadTimer = ThreadTimer(interval)
    threadTimer.start()
    
    thread = threading.Thread(target=task)
    thread.start()
    #time.sleep(5)
    print("---END---")
    sys.exit()  



if __name__ == '__main__':
    main()

#---END---