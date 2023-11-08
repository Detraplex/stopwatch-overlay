"""
main handler of the clock module for settings and clock module
Detraplex
labeled for free, individual use
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
    def __init__(self, myapp) -> None:
        """Setup and deploy for the whole clock application"""
        self.myapp = myapp
        self.name = [self.generate_main, self.generate_settings]
        self.main()
        

    def thread_function(self):
        threads = list()
        for index in range(2):
            logger.info("Main      : Created and thread %d starting", index)
            stich = threading.Thread(target=self.name[index], args=())
            threads.append(stich)
            stich.start()

        for i, thread in enumerate(threads):
            logger.info("Main      : before joining thread %d", i)
            time.sleep(.2)
            thread.join()
            logger.info("Main      : Thread %d done", i)


    def generate_main(self):
        logger.info("Generate Main      : Initalize")
        main_root = tk.Tk()
        main_root.title("Clock Overlay")
        #main_root.geometry('300x300')
        clock_app = clock.App(main_root, main_root, self.myapp)
        main_root.mainloop()
        logger.info("Generate Main      : Done")
        return clock_app

    def generate_settings(self):
        logger.info("Generate Settings      : Initalize")
        settings_root = tk.Tk()
        settings_root.title("Clock Settings")
        #settings_root.geometry('300x300')
        settings_app = settings.App(settings_root,self.myapp)
        settings_root.mainloop()
        logger.info("Generate settings      : Done")
        return settings_app

    def main(self):
        logger.info("Main Start     : Initalize")
        self.thread_function()

    def send_times(self, h, m, s, ms):
        logger.info("Reciving times:      Start")
        logger.info("Sending times:      Start")
        self.clock_app.recive_times(self.clock_app, h,m,s,ms)
        logger.info("Sending times:      End")
        

if __name__ == "__main__":
    myapp = Main
    Main(myapp)