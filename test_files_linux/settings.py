"""
testing for settings of the clock module
"""

import tkinter as tk
import os
from sys import path
path.insert(0, os.getcwd())
import clock_main_test as main


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.quitButton = tk.Button(self, text = 'Quit', command = self.close_windows)
        self.enter_button = tk.Button(self, text = "Enter", command=self.get_entry)
        self.entry = tk.Entry(self)
        self._ = tk.Label(self, text= " ", font=(15))
        self.pack()
        self.initalize()

    def initalize(self):
        self.quitButton.grid(row = 1, column = 2)
        self._.grid(row = 0, column = 0)
        self._.grid(row = 2, column = 0)
        self._.grid(row = 1, column = 1)
        self.entry.grid(row = 0, column = 1)
        self.enter_button.grid(row = 1, column = 0)

    def close_windows(self):
        self.master.destroy()
    
    def get_entry(self):
        piss = self.entry.get()
        print(piss)
        return self.entry.get()
