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
    
    def __mute_a__(self, num: int, sub_plus: int, op) -> int:
        """returns add/sub of hours:
        num: self.a
        sub_plus: "+", "-"
        """
        if op == '-':
            self.a = num - sub_plus
        elif op == '+':
            self.a = num + sub_plus

    def __mute_b__(self, num: int, sub_plus: int, op) -> int:
        """returns add/sub of minutes:
        num: self.s
        sub_plus: "+", "-"
        """
        if op == '-':
            self.b = num - sub_plus
        elif op == '+':
            self.b = num + sub_plus

    def __mute_c__(self, num: int, sub_plus: int, op) -> int:
        """returns add/sub of seconds:
        num: self.c
        sub_plus: "+", "-"
        """
        if op == '-':
            self.c = num - sub_plus
        elif op == '+':
            self.c = num + sub_plus

    def __mute_d__(self, num: int, sub_plus: int, op) -> int:
        """returns add/sub of miliseconds:
        num: self.d
        sub_plus: "+", "-"
        """
        if op == '-':
            self.d = num - sub_plus
        elif op == '+':
            self.d = num + sub_plus

    def __list_vals__(self) -> dict:
        """returns the list of key, tkinter button pairs"""
        return self.buttons_and_such

    def add_time(self):
        """adds a minute to the current time"""
        self.__mute_b__(self.__b__(), 1, '+')
        self.after(0, self.sub_countdown)
        
    def sub_time(self):
        """subtracts a minute from the current time"""
        self.__mute_b__(self.__b__(), 1, '-')
        self.after(0, self.sub_countdown)
    
    def test_neg(self, hour_input: str, minute_input: str, second_input: str, milisecond_input: str) -> bool:
        list_of_stuff = [hour_input, minute_input, second_input, milisecond_input]
        for i in list_of_stuff:
            for j in i:
                if j == '-':
                    return False
                else:
                    continue
        return True

    def starting(self):
        """starts the timer early"""
        self.timer_face.configure(text="Have I Started Yet?")
        self.__mute_a__(self.__a__(), self.__a__(), '-')
        self.__mute_b__(self.__b__(), self.__b__(), '-')
        self.__mute_c__(self.__c__(), self.__c__(), '-')
        self.__mute_d__(self.__d__(), self.__d__(), '-')
        root.after_cancel(self.__job)
        self.__job = None

    def sub_countdown(self):
        """starts counting down from an inputed time"""
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
    
    def test_exist(self, hour_input, minute_input, second_input, milisecond_input) -> bool:
        if (hour_input == '') or (minute_input == '') or (second_input == '') or (milisecond_input == ''):
            return False
        else:
            return True
    
    def time_reformatter(self) -> str:
        """fix for the formatting bug, badly but it works (if statements will be fixed later)"""
        print("put time in now, either two didgets or one where a zero starts the number (ex: 01 for 1)")
        hour_input = input('hour: ')
        minute_input = input('minute: ')
        second_input = input('second: ')
        milisecond_input = input('milisecond: ')
        if (len(hour_input) > 2) or (len(minute_input) > 2) or (len(second_input) > 2) or (len(milisecond_input) > 4) or (self.test_exist(hour_input, minute_input, second_input, milisecond_input) != True):
            return None
        elif self.test_neg(hour_input, minute_input, second_input, milisecond_input) == False:
            return None
        elif (hour_input[0].isdigit() == False) or (hour_input[1].isdigit() == False):
            return None
        elif (hour_input[0] == '2') and (hour_input[1] not in ['0', '1', '2', '3', '4']):
            return None
        elif (minute_input[0].isdigit() == False) or (minute_input[1].isdigit() == False):
            return None
        elif (second_input[0].isdigit() == False) or (second_input[1].isdigit() == False):
            return None
        elif (milisecond_input[0].isdigit() == False) or (milisecond_input[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']):
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
                print('use an int please')
            else:
                pp = 0
                for i in time_input:
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
        """initalizes the stopwatch"""
        self.__job = None
        try:
            self.timer()
        except:
            self.__job = self.after(0, self.initalize)
    
    def timer(self):
        """starts counting up from 00:00:00:0000"""
        self.__job = None
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
        """formats where the buttins and time go"""
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
