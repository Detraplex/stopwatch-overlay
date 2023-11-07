import time
import clock

def runtime(clock):
    start_time = time.time()
    clock.time_reformatter()
    end_time = start_time - time.time()
    print(end_time)

if __name__ == "__main__": 
    clock = clock.App
    runtime(clock)