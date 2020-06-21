# mashToPlayHigh.py

from pynput import keyboard
import time


def callb(key):  # what to do on key-release
    # converting float to str, slicing the float
    ti1 = str(time.time() - t)[0:5]
    print(ti1)
    presses.append(float(ti1))
    return False  # stop detecting more key-releases


def callb1(key):  # what to do on key-press
    return False  # stop detecting more key-presses

presses = []

for i in range(20):
    t = time.time()
    # setting code for listening key-press
    

      # reading time in sec

    # setting code for listening key-release
    with keyboard.Listener(on_release=callb) as listener:
        listener.join()
listener.stop()

print(presses)
print(sum(presses)/len(presses))
if sum(presses)/len(presses) >= 0.7:
    print('you did not press fast enough')
else:
    print('you did press fast enough')
import sys
sys.exit()
