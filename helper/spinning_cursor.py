import itertools
import sys
import time


def spinning_cursor(stop_event):
    spinner = itertools.cycle(['-', '/', '|', '\\'])
    while not stop_event.is_set():
        sys.stdout.write(next(spinner))  
        sys.stdout.flush()               
        sys.stdout.write('\b')           
        time.sleep(0.1)
