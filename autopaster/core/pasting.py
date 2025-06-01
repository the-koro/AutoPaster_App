import keyboard
import time
import random

def paste(interval, random_offset, max_paste_times, press_enter=False, accurate_enter=False):
    keyboard.press_and_release('ctrl+v')
    if press_enter:
        if accurate_enter:
            time.sleep(0.02)
            keyboard.press_and_release('enter')
        else:
            keyboard.press_and_release('enter')
    if interval > 0:
        if random_offset > 0:
            time.sleep(interval + random.uniform(0, random_offset))
        else:
            time.sleep(interval)