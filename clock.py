import tkinter as tk

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
        self._ =tk.Label(self, text= " ", font=(15), width=10)
        self.stopwatch_button = tk.Button(self, text = 'StopWatch', command = self.stopwatch)
        self.countdown_button = tk.Button(self, text = 'CountDown', command = self.countdown)
        self.buttons_and_such = {"_":self._,"timer_face":self.timer_face, "add_time_button":self.add_time_button, "sub_time_button":self.sub_time_button, "starting_button":self.starting_button}
        self.pack()
        self.initalize()

    def __a__(self) -> int:
        return self.a
    
    def __b__(self) -> int:
        return self.b
    
    def __c__(self) -> int:
        return self.c
    
    def __d__(self) -> int:
        return self.d
    
    def __mute_a__(self, num: int, sub_plus: int, op) -> int:
        if op == '-':
            self.a = num - sub_plus
        elif op == '+':
            self.a = num + sub_plus

    def __mute_b__(self, num: int, sub_plus: int, op) -> int:
        if op == '-':
            self.b = num - sub_plus
        elif op == '+':
            self.b = num + sub_plus

    def __mute_c__(self, num: int, sub_plus: int, op) -> int:
        if op == '-':
            self.c = num - sub_plus
        elif op == '+':
            self.c = num + sub_plus

    def __mute_d__(self, num: int, sub_plus: int, op) -> int:
        if op == '-':
            self.d = num - sub_plus
        elif op == '+':
            self.d = num + sub_plus

    def __list_vals__(self) -> list:
        return self.penis

    def add_time(self):
        self.__mute_b__(self.__b__(), 1, '+')
        self.after(0, self.sub_countdown)
        
    def sub_time(self):
        self.__mute_b__(self.__b__(), 1, '-')
        self.after(0, self.sub_countdown)
    
    def starting(self):
        self.timer_face.configure(text="Have I Started Yet?")
        root.after_cancel(self.__job)
        self.__job = None

    def sub_countdown(self):
        if (self.__d__() <= 1000) & (self.__d__() != 00): #as long as mili doesn equal zero subtract one till it is
            self.__mute_d__(self.__d__(), 1, '-')
            self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
            self.__job =self.after(1, self.sub_countdown)
        elif (self.c <= 60) & (self.c != 00): #if second doesnt equal zero and is less than or equal to 60 then subtract a sec and add 999 mili
                self.__mute_c__(self.__c__(), 1, '-')
                self.__mute_d__(self.__d__(), 999, '+')
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job =self.after(1, self.sub_countdown)
        elif (self.__b__() <= 60) & (self.__b__() != 00): #if minute is not zero and less than or equal to 60 than subtract min,sec and add one 999 mili
                self.__mute_b__(self.__b__(), 1, '-')
                self.__mute_c__(self.__c__(), 60, '+')
                self.__mute_c__(self.__c__(), 1, '-')
                self.__mute_d__(self.__d__(), 999, '+')
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job =self.after(1, self.sub_countdown)
        elif (self.__a__() <= 24) & (self.__a__() != 00): #if the hour is smaller than 24 and doesn equal zero then subtract min, sec, hour by one and add 999 to mili
                self.__mute_a__(self.__a__(), 1, '-')
                self.__mute_b__(self.__b__(), 60, '+')
                self.__mute_b__(self.__b__(), 1, '-')
                self.__mute_c__(self.__c__(), 60, '+')
                self.__mute_c__(self.__c__(), 1, '-')
                self.__mute_d__(self.__d__(), 999, '+')
                self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
                self.__job = self.after(1, self.sub_countdown)
        else:
                self.timer_face.configure(text="Have I Started Yet?")
                self.__job = self.after(0, self.initalize)
    
    def countdown(self):
        if self.t_f == True:
            pissmaster = input("put time in now:")
            pissmaster = pissmaster.split(":")
            pp = 0
            for i in pissmaster:
                if pp == 0:
                    self.__mute_a__(int(i), 0 , '-')
                    pp = pp + 1
                elif pp == 1:
                    self.__mute_b__(int(i), 0, '-')
                    pp = pp + 1
                elif pp == 2:
                   self.__mute_c__(int(i), 0, '-')
                   pp = pp + 1
                elif pp == 3:
                   self.__mute_d__(int(i), 0 ,'-')
                   pp = pp + 1
            self.t_f = False
            self.timer_face.configure(text="{}:{}:{}:{}".format(self.__a__() ,self.__b__(), self.__c__(), self.__d__()))
            self.__job = self.after(0, self.sub_countdown)
    
    def stopwatch(self):
        try:
            self.timer()
        except:
            self.__job = self.after(0, self.initalize)
    
    def timer(self):
        try:
            if self.__d__() == 1000:
                self.__mute_d__(0000, 0, '-')
                self.__mute_c__(self.__c__(), 1, '+')
            elif self.__c__() == 60:
                self.__mute_c__(self.__c__(), 60, '-')
                self.__mute_b__(self.__b__(), 1, '+')
            elif self.__b__() == 60:
                self.__mute_b__(self.__b__(), 60, '-')
                self.__mute_a__(self.__a__(), 1, '+')
            elif self.__a__() == 24:
                self.__mute_a__(self.__a__(), self.__a__, '-')
                self.__mute_b__(self.__b__(), self.__b__, '-')
                self.__mute_c__(self.__c__(), self.__c__, '-')
                self.__mute_s__(self.__d__(), self.__d__, '-')
            else:
                self.__mute_d__(self.__d__(), 1, '+')
            self.timer_face.configure(text="{}:{}:{}:{}".format(self.a ,self.b, self.c, self.d))
            self.__job = self.after(1, self.timer)
        except:
            self.__job = self.after(0, self.initalize)
    
    def initalize(self):
        self._.grid(row = 0, column = 0)
        self.add_time_button.grid(row = 1, column = 0)
        self.sub_time_button.grid(row = 1, column = 2)
        self.starting_button.grid(row = 1, column = 1)
        self.timer_face.grid(row = 0, column = 1)
        self._.grid(row = 0, column = 2)
        self._.grid(row = 2, column = 1)
        self.stopwatch_button.grid(row = 2, column = 0)
        self.countdown_button.grid(row = 2, column = 2)


root = tk.Tk()
myapp = App(root)
root.title("clock overlay")
root.mainloop()
