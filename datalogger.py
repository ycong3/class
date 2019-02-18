from microbit import *
import time
while True:
    time.sleep(1)
    temp = temperature()
    comp = compass.heading()
    print(comp, temp, sep=',')

