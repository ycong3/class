# Write your code here :-)
from microbit import *

# define our function
def weather_conditions(temp, condition):
    # temperature
    # temp = 84.4
    # conditions
    # condition = "dry"
    # scroll the current conditions
    # TODO
    display.scroll(temp)
    display.scroll(condition)

def c_to_f(ctemp):
    ftemp = ((9/5)*ctemp) + 32
    return ftemp


while True:
    if button_a.is_pressed():
        # mbctemp = temperature()
        mbftemp = c_to_f(temperature())
        weather_conditions(mbftemp, "rainy")
    elif (button_b.is_pressed()):
        display.show("B")


import time
while True:
    time.sleep(0.05)
    reading = pin2.read_analog()
    print((reading,))