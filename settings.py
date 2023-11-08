"""
Settings of the clock module
Detraplex
labeled for free, individual use
"""

import tkinter as tk
import os
from sys import path
path.insert(0, os.getcwd())
import main


class App(tk.Frame):
    def __init__(self, master, main_app) -> None:
        super().__init__(master)
        self.main_app = main_app
        self.quitButton = tk.Button(self, text = 'Quit', command = self.close_windows)
        self.enter_button = tk.Button(self, text = "Enter", command=self.send_times)
        self.entry_hour = tk.Entry(self)
        self.entry_minute = tk.Entry(self)
        self.entry_second = tk.Entry(self)
        self.entry_milisecond = tk.Entry(self)
        self._ = tk.Label(self, text= " ", font=(15))
        self.pack()
        self.initalize()

    def initalize(self):
        self.quitButton.grid(row = 1, column = 2)
        self._.grid(row = 0, column = 0)
        self._.grid(row = 2, column = 0)
        self.entry_hour.grid(row = 0, column = 1)
        self.entry_minute.grid(row = 1, column = 1)
        self.entry_second.grid(row = 2, column = 1)
        self.entry_milisecond.grid(row = 3, column = 1)
        self.enter_button.grid(row = 1, column = 0)

    def close_windows(self):
        self.master.destroy()
    
    def get_entry_h(self):
        return self.entry_hour.get()

    def get_entry_m(self):
        return self.entry_minute.get()

    def get_entry_s(self):
        return self.entry_second.get()

    def get_entry_ms(self):
        return self.entry_milisecond.get()
    
    def send_times(self):
        h = self.get_entry_h()
        m = self.get_entry_m()
        s = self.get_entry_s()
        ms = self.get_entry_ms()
        self.main_app.send_times(self.main_app, h,m,s,ms)

