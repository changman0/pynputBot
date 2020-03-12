# For 4 windows
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(8)
reps = 0
while reps < 1000:
    for i in range(4):
        keyboard.press('\t')
        keyboard.release('\t')
        keyboard.press(' ')
        keyboard.release(' ')
        time.sleep(0.1)
        
        for j in range(5):
            keyboard.press('\t')
            keyboard.release('\t')

        time.sleep(0.1)
        keyboard.press('\r')
        keyboard.release('\r')

        time.sleep(0.8)
    
        keyboard.press(Key.alt)
        for k in range(3):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.1)                        
        keyboard.release(Key.alt)

        time.sleep(0.8)

    for l in range(4):        
        for m in range(2):
            keyboard.press('\t')
            keyboard.release('\t')

        time.sleep(0.1)
        keyboard.press('\r')
        keyboard.release('\r')

        time.sleep(0.8)
        
        keyboard.press(Key.alt)
        for k in range(3):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.1)
        keyboard.release(Key.alt)

        time.sleep(0.8)
    reps += 1
