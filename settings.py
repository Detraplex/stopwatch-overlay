"""
Settings of the clock module
"""

import tkinter as tk
import os
from sys import path
path.insert(0, os.getcwd())
import main


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.quitButton = tk.Button(self, text = 'Quit', command = self.close_windows)
        self.enter_button = tk.Button(self, text = "Enter", command=self.save_entry)
        self.entry = tk.Entry(self)
        self.start = tk.Button(self, text = "Start", command = self.send_times)
        self._ = tk.Label(self, text= " ", font=(15))
        self.pack()
        self.initalize()
        self.counter = 0
        self.a = 00
        self.b = 00
        self.c = 00
        self.d = 0000

    def initalize(self):
        self.start.grid(row = 0, column=0)
        self.entry.grid(row = 0, column = 1)
        self.enter_button.grid(row=0, column=2)
        self._.grid(row = 1, column = 0)
        self._.grid(row = 1, column = 2)
        self.quitButton.grid(row = 1, column = 1)

    def close_windows(self):
        self.master.destroy()
    
    def get_entry(self, entry: str) -> int:
        return self.entry

    def mute_a(self, num: int):
        self.a = num

    def mute_b(self, num: int):
        self.b = num

    def mute_c(self, num: int):
        self.c = num

    def mute_d(self, num: int):
        self.d = num

    def switch(self):
        if self.counter == 0:
            self.counter += 1
            self.mute_a(self.get_entry())
        elif self.counter == 1:
            self.counter += 1
            self.mute_b(self.get_entry())
        elif self.counter == 2:
            self.counter += 1
            self.mute_c(self.get_entry())
        elif self.counter == 3:
            self.counter += 1
            self.mute_d(self.get_entry())

    def save_entry(self):
        if self.counter == 4:
            print("No")
        else:
            self.switch()

    def get_entry(self):
        return self.entry.get()

    def send_times(self):
        if self.counter == 4:
            self.counter = 0
            times = list()
            for i in range(5):
                times[i] = self.get_entry()
        else:
            print("you have to add all of the fields")
