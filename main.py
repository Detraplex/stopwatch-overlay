"""
main handler of the clock module for settings and clock module
"""

import tkinter as tk
import threading
import logging as log
import os
import time
from sys import path
path.insert(0, os.getcwd())
import clock
import settings

log.basicConfig(level=log.NOTSET)
handle = "main"
logger = log.getLogger("main")

class Main:
    def __init__(self) -> None:
        """Setup and deploy for the whole clock application"""
        self.name = [self.generate_main, self.generate_settings]
        self.main()

    def thread_function(self):
        logger.info("Main      : Created and thread %d starting", 0)
        logger.info("Main      : Created and thread %d starting", 1)
        logger.info("Main      : before joining thread %d", 0)
        self.generate_main()
        logger.info("Main      : before joining thread %d", 1)
        self.generate_settings()
        logger.info("Main      : Thread %d done", 0)
        logger.info("Main      : Thread %d done", 1)
        tk.mainloop()

    def generate_main(self):
        logger.info("Generate Main      : Initalize")
        main_root = tk.Tk()
        main_root.title("Clock Overlay")
        #main_root.geometry('300x300')
        self.my_app_m = clock.App(main_root, main_root)
        logger.info("Generate Main      : Done")
        return True

    def generate_settings(self):
        logger.info("Generate Settings      : Initalize")
        settings_root = tk.Tk()
        settings_root.title("Clock Settings")
        #settings_root.geometry('300x300')
        self.my_app_s = settings.App(settings_root)
        logger.info("Generate settings      : Done")
        return True

    def send_times(self, times: list):
        print("piss")
        

    def main(self):
        logger.info("Main Start     : Initalize")
        self.thread_function()
        
if __name__ == "__main__":
    Main()