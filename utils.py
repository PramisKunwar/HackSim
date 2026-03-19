import time
import sys
import os
from colors import green, yellow, cyan, red, bold

def slow_print(t, d=0.03):
    for ch in t: 
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(d)
    print()

def animated_print(lines, d=0.6):
    for l in lines: 
        slow_print(l, 0.02)
        time.sleep(d)

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')