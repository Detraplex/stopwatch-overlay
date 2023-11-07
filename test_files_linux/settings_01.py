"""
testing for settings of the clock module
"""

import tkinter as tk
import os
from sys import path
path.insert(0, os.getcwd())
import clock_main_test as main

class App(tk.Frame):
    def __init__(self) -> None:
        self.frame = tk.Frame(self.master)