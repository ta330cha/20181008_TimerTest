##!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
from datetime import datetime

class ThreadTimer(threading.Timer):
    def __init__(self, interval):
        self.interval = interval
    
    def start(self):
        thread = threading.Thread(target=self.__task)
        thread.start()
    
    def __task(self):
        print("ThreadTimer---{}".format(datetime.now().strftime("%Y/%m/%d %H:%M.%S")))
        thread = threading.Timer(self.interval, self.__task)
        thread.start()

#---END---