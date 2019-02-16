from microbit import *

# loop 10 times
# random gives me a 1 or 2
# if it's a 1 count as a head
# if it's a 2 count as a tail
# output results to user

import random

heads = 0
tails = 0

while True:
    if accelerometer.was_gesture("shake"):
        for eachshake in range(1, 11):
            num = random.randint(1,2)
            if(num == 1):
                display.show("H")
                heads += 1
            else:
                display.show("T")
                tails += 1
            sleep(1000)
        display.scroll(str(heads)+ "H" + str(tails)+ "T")
        heads = 0
        tails = 0