"""
stopwatch and integrated timer
Detraplex
labeled for free, individual use
"""

import tkinter as tk
from playsound import playsound
import logging as log

log.basicConfig(level=log.NOTSET)
handle = "clock"
logger = log.getLogger("clock")


class App(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.t_f = True
        self.__job = None
        self.a = 00
        self.b = 00
        self.c = 00
        self.d = 0000
        self.timer_face = tk.Label(self, text = '00:00:00:0000', font=(15), width=15)
        self.add_time_button = tk.Button(self, text = '+', command = self.add_time)
        self.sub_time_button = tk.Button(self, text = '-', command = self.sub_time)
        self.starting_button = tk.Button(self, text = 'Start Early', command = self.starting)
        self.quit_button = tk.Button(self, text = "Quit", command = self.close_window)
        self._ = tk.Label(self, text= " ", font=(15), width=10)
        self.stopwatch_button = tk.Button(self, text = 'StopWatch', command = self.stopwatch)
        self.countdown_button = tk.Button(self, text = 'CountDown', command = self.countdown)
        self.buttons_and_such = {"_":self._,"timer_face":self.timer_face, "add_time_button":self.add_time_button, "sub_time_button":self.sub_time_button, "":self.quit_button, "starting_button":self.starting_button}
        self.pack()
        self.initalize()

    def __a__(self) -> int:
        """returns hours"""
        return self.a
    
    def __b__(self) -> int:
        """returns minutes"""
        return self.b
    
    def __c__(self) -> int:
        """returns seconds"""
        return self.c
    
    def __d__(self) -> int:
        """returns miliseconds"""
        return self.d
    
    def __mute_a_add__(self, num: int, add: int) -> int:
        """returns addition of hours:
        num: self.a
        add: time to add
        """
        self.a = num + add

    def __mute_b_add__(self, num: int, add: int) -> int:
        """returns addition of hours:
        num: self.b
        add: time to add
        """
        self.b = num + add

    def __mute_c_add__(self, num: int, add: int) -> int:
        """returns addition of hours:
        num: self.c
        add: time to add
        """
        self.c = num + add

    def __mute_d_add__(self, num: int, add: int) -> int:
        """returns addition of hours:
        num: self.d
        add: time to add
        """
        self.d = num + add

    def __mute_a_sub__(self, num: int, sub: int) -> int:
        """returns subtraction of hours:
        num: self.a
        sub: time to subtract
        """
        self.a = num - sub

    def __mute_b_sub__(self, num: int, sub: int) -> int:
        """returns subtraction of hours:
        num: self.b
        sub: time to subtract
        """
        self.b = num - sub

    def __mute_c_sub__(self, num: int, sub: int) -> int:
        """returns subtraction of hours:
        num: self.c
        sub: time to subtract
        """
        self.c = num - sub

    def __mute_d_sub__(self, num: int, sub: int) -> int:
        """returns subtraction of hours:
        num: self.d
        sub: time to subtract
        """
    
        self.d = num - sub
    

    def __list_vals__(self) -> dict:
        """returns the list of key, tkinter button pairs"""
        return self.buttons_and_such

    def add_time(self):
        """adds a minute to the current time"""
        self.__mute_b_add__(self.__b__(), 1)
        self.after(0, self.sub_countdown)
        
    def sub_time(self):
        """subtracts a minute from the current time"""
        self.__mute_b_sub__(self.__b__(), 1)
        self.after(0, self.sub_countdown)


    def play(self):
        """plays ending sound for timer"""
        logger.info("Playing sound:     START")
        playsound('./sound_files/alarm-clock-short-6402.mp3')
        logger.info("Playing sound:     END")

    def starting(self):
        """starts the timer early"""
        self.timer_face.configure(text="Have I Started Yet?")
        self.__mute_a_sub__(self.__a__(), self.__a__())
        self.__mute_b_sub__(self.__b__(), self.__b__())
        self.__mute_c_sub__(self.__c__(), self.__c__())
        self.__mute_d_sub__(self.__d__(), self.__d__())
        self.after_cancel(self.__job)
        self.__job = None

    def sub_countdown(self):
        """starts counting down from an inputed time"""
        if (self.__d__() <= 1000) & (self.__d__() != 00): #as long as mili doesn equal zero subtract one till it is
            self.__mute_d_sub__(self.__d__(), 1)
            self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
            self.__job =self.after(1, self.sub_countdown)
        elif (self.c <= 60) & (self.c != 00): #if second doesnt equal zero and is less than or equal to 60 then subtract a sec and add 999 mili
                self.__mute_c_sub__(self.__c__(), 1)
                self.__mute_d_add__(self.__d__(), 999)
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job =self.after(1, self.sub_countdown)
        elif (self.__b__() <= 60) & (self.__b__() != 00): #if minute is not zero and less than or equal to 60 than subtract min,sec and add one 999 mili
                self.__mute_b_sub__(self.__b__(), 1)
                self.__mute_c_add__(self.__c__(), 60)
                self.__mute_c_sub__(self.__c__(), 1)
                self.__mute_d_add__(self.__d__(), 999)
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job =self.after(1, self.sub_countdown)
        elif (self.__a__() <= 24) & (self.__a__() != 00): #if the hour is smaller than 24 and doesn equal zero then subtract min, sec, hour by one and add 999 to mili
                self.__mute_a_sub__(self.__a__(), 1)
                self.__mute_b_add__(self.__b__(), 60)
                self.__mute_b_sub__(self.__b__(), 1)
                self.__mute_c_add__(self.__c__(), 60)
                self.__mute_c_sub__(self.__c__(), 1)
                self.__mute_d_add__(self.__d__(), 999)
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job = self.after(1, self.sub_countdown)
        else:
                self.timer_face.configure(text="Have I Started Yet?")
                self.__job = self.after(0, self.initalize)
                self.play()
    
 
    def time_reformatter(self) -> str:
        """checks edge cases confirms assumptions"""
        print("put time in now, either two didgets or one where a zero starts the number (ex: 01 for 1)")
        hour_input = input('hour: ')
        minute_input = input('minute: ')
        second_input = input('second: ')
        milisecond_input = input('milisecond: ')
        
        num_list = [hour_input, minute_input, second_input, milisecond_input] 

        for i in num_list:#check for uninitalized variables
            if i != '':
                if i.isdigit() == True:  
                    continue
            return None

        if len(num_list.pop()) > 4: #must be at most 4 miliseconds
            return None

        for i in num_list: # two diget int for hour, min and sec
            if len(i) > 2:
                return None
            continue

        if (hour_input[0] == '2') and (hour_input[1] not in ['0', '1', '2', '3', '4']):
            return None

        else:   
            return hour_input,minute_input,second_input,milisecond_input

    def countdown(self):
        """initalizes the countdown"""
        self.__job = None
        self.t_f = True
        if self.t_f == True:
            time_input = self.time_reformatter()
            if time_input == None:
                self.__job = None
                print('refer to instructions and try again')
            else:
                count = 0
                for i in time_input:
                    if count == 0:
                        self.__mute_a_sub__(int(i), 0)
                        count += 1
                    elif count == 1:
                        self.__mute_b_sub__(int(i), 0)
                        count += 1
                    elif count == 2:
                       self.__mute_c_sub__(int(i), 0)
                       count += 1
                    elif count == 3:
                       self.__mute_d_sub__(int(i), 0)
                       count += 1
                self.t_f = False
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job = self.after(0, self.sub_countdown)
    
    def stopwatch(self):
        """initalizes the stopwatch"""
        self.__job = None
        try:
            self.timer()
        except:
            self.__job = self.after(0, self.initalize)
    
    def close_window(self):
        logger.info("Window:    CLOSED")
        self.master.destroy()

    def timer(self):
        """starts counting up from 00:00:00:0000"""
        self.__job = None
        try:
            if self.__d__() == 1000:
                self.__mute_d_sub__(0000, 0)
                self.__mute_c_add__(self.__c__(), 1)
            elif self.__c__() == 60:
                self.__mute_c_sub__(self.__c__(), 60)
                self.__mute_b_add__(self.__b__(), 1)
            elif self.__b__() == 60:
                self.__mute_b_sub__(self.__b__(), 60)
                self.__mute_a_add__(self.__a__(), 1)
            elif self.__a__() == 24:
                self.__mute_a_sub__(self.__a__(), self.__a__())
                self.__mute_b_sub__(self.__b__(), self.__b__())
                self.__mute_c_sub__(self.__c__(), self.__c__())
                self.__mute_d_sub__(self.__d__(), self.__d__())
            else:
                self.__mute_d_add__(self.__d__(), 1)
            self.timer_face.configure(text="{}:{}:{}:{}".format(self.a ,self.b, self.c, self.d))
            self.__job = self.after(1, self.timer)
        except:
            self.__job = self.after(0, self.initalize)
    
    def initalize(self):
        """formats where the buttons and time go"""
        self._.grid(row = 0, column = 0)
        self.add_time_button.grid(row = 1, column = 0)
        self.sub_time_button.grid(row = 1, column = 2)
        self.starting_button.grid(row = 1, column = 1)
        self.timer_face.grid(row = 0, column = 1)
        self._.grid(row = 0, column = 2)
        self.quit_button.grid(row = 2, column = 1)
        self.stopwatch_button.grid(row = 2, column = 0)
        self.countdown_button.grid(row = 2, column = 2)

if __name__ == "__main__":
    main_root = tk.Tk()
    main_root.title("Clock Overlay")
    main_root.geometry('400x100')
    my_app = App(main_root)
    main_root.mainloop()